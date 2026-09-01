# mac-clipboard-cleaner

`pbclean` is a tiny, privacy-friendly command-line tool for cleaning text copied
from PDFs and web pages on macOS. It is designed to remove invisible Unicode
characters, normalize line endings, and make pasted text easier to reuse.

The project uses only Python's standard library. Text is processed locally and
is never uploaded anywhere.

## Planned features

- Clean text from standard input or a file.
- Remove zero-width and byte-order-mark characters.
- Normalize non-breaking spaces and line endings.
- Read from and write back to the macOS clipboard.

## License

MIT
