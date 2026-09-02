#!/usr/bin/env python3
"""Fetch authoritative corpus PDFs and record retrieval status.

Retrieval is not the same as FULL_TEXT_READ. Promote a record only after the
relevant main text, Methods, figures/captions, and Discussion are inspected.
"""

import argparse
import csv
import subprocess
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path


def command(args):
    return subprocess.run(args, capture_output=True, text=True, timeout=180)


def valid_pdf(path):
    if not path.exists() or path.stat().st_size < 1024:
        return False
    with path.open("rb") as handle:
        return handle.read(5) == b"%PDF-"


def fetch(row, pdf_dir, text_dir):
    result = dict(row)
    result.update(
        retrieval="FAILED",
        http_status="",
        content_type="",
        bytes=0,
        pages=0,
        words=0,
        error="",
    )
    pdf_path = pdf_dir / f"{row['year']}_{row['slug']}.pdf"
    text_path = text_dir / f"{row['year']}_{row['slug']}.txt"
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; Baker-manuscript-corpus/1.0)",
        "Accept": "application/pdf,text/html;q=0.8,*/*;q=0.5",
    }

    if valid_pdf(pdf_path):
        result["http_status"] = "cached"
        result["content_type"] = "application/pdf"
    else:
        last_error = ""
        for attempt in range(3):
            try:
                request = urllib.request.Request(row["source_url"], headers=headers)
                with urllib.request.urlopen(request, timeout=180) as response:
                    result["http_status"] = response.status
                    result["content_type"] = response.headers.get("content-type", "")
                    with pdf_path.open("wb") as handle:
                        while True:
                            chunk = response.read(1024 * 1024)
                            if not chunk:
                                break
                            handle.write(chunk)
                if not valid_pdf(pdf_path):
                    raise ValueError("response was not a complete PDF")
                break
            except Exception as exc:
                last_error = f"{type(exc).__name__}: {exc}"
                pdf_path.unlink(missing_ok=True)
                if attempt < 2:
                    time.sleep(2**attempt)
        else:
            result["error"] = last_error
            return result

    result["bytes"] = pdf_path.stat().st_size
    info = command(["pdfinfo", str(pdf_path)])
    if info.returncode != 0:
        result["error"] = "pdfinfo failed: " + info.stderr.strip()[:300]
        return result
    for line in info.stdout.splitlines():
        if line.startswith("Pages:"):
            result["pages"] = int(line.split(":", 1)[1].strip())

    extracted = command(["pdftotext", str(pdf_path), str(text_path)])
    if extracted.returncode != 0:
        result["error"] = "pdftotext failed: " + extracted.stderr.strip()[:300]
        return result
    text = text_path.read_text(errors="replace")
    result["words"] = len(text.split())
    if result["pages"] >= 2 and result["words"] >= 800:
        result["retrieval"] = "PDF_RETRIEVED"
    else:
        result["error"] = (
            f"incomplete extraction: {result['pages']} pages, "
            f"{result['words']} words"
        )
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--workers", type=int, default=6)
    args = parser.parse_args()

    pdf_dir = args.output_dir / "pdf"
    text_dir = args.output_dir / "text"
    pdf_dir.mkdir(parents=True, exist_ok=True)
    text_dir.mkdir(parents=True, exist_ok=True)

    with args.manifest.open(newline="") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))

    results = []
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {
            pool.submit(fetch, row, pdf_dir, text_dir): row for row in rows
        }
        for future in as_completed(futures):
            item = future.result()
            results.append(item)
            print(f"{item['retrieval']:<14} {item['year']} {item['slug']}", flush=True)

    results.sort(key=lambda item: (-int(item["year"]), item["slug"]))
    original_fields = list(rows[0])
    extra_fields = [
        "retrieval", "http_status", "content_type", "bytes", "pages", "words", "error"
    ]
    with (args.output_dir / "access-status.tsv").open("w", newline="") as handle:
        writer = csv.DictWriter(
            handle, fieldnames=original_fields + extra_fields, delimiter="\t"
        )
        writer.writeheader()
        writer.writerows(results)


if __name__ == "__main__":
    main()
