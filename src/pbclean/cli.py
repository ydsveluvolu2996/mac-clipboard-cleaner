"""Command-line interface for pbclean."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

from . import __version__
from .clipboard import ClipboardError, copy_to_clipboard, read_clipboard
from .cleaner import clean_text


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="pbclean",
        description="Clean invisible characters and awkward whitespace from text.",
    )
    parser.add_argument(
        "path",
        nargs="?",
        type=Path,
        help="UTF-8 text file to clean; reads standard input when omitted",
    )
    parser.add_argument(
        "--keep-trailing-whitespace",
        action="store_true",
        help="preserve spaces and tabs at the ends of lines",
    )
    parser.add_argument(
        "--clipboard",
        action="store_true",
        help="read text from the macOS clipboard instead of standard input",
    )
    parser.add_argument(
        "--copy",
        action="store_true",
        help="write cleaned text to the macOS clipboard instead of standard output",
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.clipboard and args.path:
        parser.error("path and --clipboard cannot be used together")

    try:
        if args.clipboard:
            source = read_clipboard()
        elif args.path:
            source = args.path.read_text(encoding="utf-8")
        else:
            source = sys.stdin.read()
    except (OSError, UnicodeError, ClipboardError) as error:
        parser.error(str(error))

    result = clean_text(
        source,
        trim_trailing_whitespace=not args.keep_trailing_whitespace,
    )
    if args.copy:
        try:
            copy_to_clipboard(result)
        except ClipboardError as error:
            parser.error(str(error))
    else:
        sys.stdout.write(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
