#!/usr/bin/env python3
"""Convert a PDS file (docx/pdf/...) to Markdown using markitdown."""

import argparse
import pathlib
import sys

from markitdown import MarkItDown


def convert(input_path: pathlib.Path, output_path: pathlib.Path) -> None:
    result = MarkItDown().convert(str(input_path))
    output_path.write_text(result.text_content, encoding="utf-8")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "input", type=pathlib.Path, help="PDS file to convert (docx, pdf, ...)"
    )
    parser.add_argument(
        "-o",
        "--output",
        type=pathlib.Path,
        help="Output .md path (default: input with .md extension)",
    )
    args = parser.parse_args()

    if not args.input.is_file():
        sys.exit(f"error: input file not found: {args.input}")

    out = args.output or args.input.with_suffix(".md")
    if out.resolve() == args.input.resolve():
        sys.exit(f"error: output would overwrite input: {out}")

    convert(args.input, out)
    print(f"Wrote {out}")
