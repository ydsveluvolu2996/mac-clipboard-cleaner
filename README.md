# mac-clipboard-cleaner

`pbclean` is a tiny, privacy-friendly command-line tool for cleaning text copied
from PDFs and web pages. It removes invisible Unicode characters, normalizes
line endings, and makes pasted text easier to reuse.

The project uses only Python's standard library. Text is processed locally and
is never uploaded anywhere.

## What it cleans

- Zero-width spaces, joiners, word joiners, and byte-order marks.
- Non-breaking and narrow non-breaking spaces.
- Windows and classic Mac line endings.
- Trailing spaces and tabs, unless you ask to preserve them.

The text's wording and paragraph structure are left intact.

## Install

```sh
python3 -m pip install .
```

## Usage

Pipe copied or generated text through `pbclean`:

```sh
printf 'Hello\u00a0world\u200b!  \r\n' | pbclean
```

Or clean a UTF-8 text file:

```sh
pbclean notes.txt > notes-clean.txt
```

To retain spaces and tabs at the ends of lines:

```sh
pbclean --keep-trailing-whitespace notes.txt
```

Native macOS clipboard integration is planned for the next release.

## License

MIT
