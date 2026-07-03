#!/usr/bin/env python3
"""Convert a PDS file (docx/pdf/...) to Markdown using markitdown."""

import argparse
import pathlib
import sys

from markitdown import MarkItDown


def convert(input_path: pathlib.Path, output_path: pathlib.Path) -> None:
    """Convert input_path to Markdown via markitdown and write it to output_path."""
    result = MarkItDown().convert(str(input_path))
    output_path.write_text(result.text_content, encoding="utf-8")


def main() -> None:
    """Parse CLI arguments and run the conversion, exiting with an error message on bad input."""
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
    input_path: pathlib.Path = args.input
    output_arg: pathlib.Path | None = args.output

    if not input_path.is_file():
        sys.exit(f"error: input file not found: {input_path}")

    out = output_arg or input_path.with_suffix(".md")
    if out.resolve() == input_path.resolve():
        sys.exit(f"error: output would overwrite input: {out}")

    convert(input_path, out)
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
