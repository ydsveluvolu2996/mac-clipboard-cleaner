# mac-clipboard-cleaner

[![CI](https://github.com/ydsveluvolu2996/mac-clipboard-cleaner/actions/workflows/ci.yml/badge.svg)](https://github.com/ydsveluvolu2996/mac-clipboard-cleaner/actions/workflows/ci.yml)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
![Runtime dependencies: 0](https://img.shields.io/badge/runtime_dependencies-0-brightgreen)

Clean invisible characters and awkward whitespace from copied text without
sending it anywhere. `pbclean` is a small command-line tool for prose copied
from PDFs, websites, chat apps, and documents. On macOS, it can clean the
clipboard in place with one command.

```console
$ printf 'Hello\u00a0world\u200b!  \r\n' | pbclean
Hello world!
```

The input above contains a non-breaking space, a zero-width space, trailing
spaces, and a Windows line ending. The output does not.

## Why pbclean?

- **Private:** processing stays on your computer.
- **Small:** the runtime uses only Python's standard library.
- **Predictable:** paragraph breaks and visible wording stay intact.
- **Scriptable:** read from the clipboard, a UTF-8 file, or standard input.
- **Native on macOS:** clipboard support uses the built-in `pbpaste` and
  `pbcopy` commands.

## Quick start

Install the latest version directly from GitHub:

```sh
python3 -m pip install \
  "git+https://github.com/ydsveluvolu2996/mac-clipboard-cleaner.git"
```

Then clean your macOS clipboard in place:

```sh
pbclean --clipboard --copy
```

For an isolated command-line installation, use
[`pipx`](https://pipx.pypa.io/):

```sh
pipx install git+https://github.com/ydsveluvolu2996/mac-clipboard-cleaner.git
```

## What it cleans

| Input problem | Result |
| --- | --- |
| Zero-width spaces, joiners, word joiners, byte-order marks | Removed |
| Non-breaking and narrow non-breaking spaces | Converted to regular spaces |
| Windows (`CRLF`) and classic Mac (`CR`) line endings | Normalized to `LF` |
| Spaces and tabs at the ends of lines | Removed by default |

`pbclean` is intended for copied prose and source text. Zero-width joiners can
be meaningful in some languages and emoji sequences, so inspect the result
before using it with text where those characters are intentional.

## Usage

Pipe copied or generated text through `pbclean`:

```sh
some-command | pbclean
```

Clean a UTF-8 text file:

```sh
pbclean notes.txt > notes-clean.txt
```

Keep spaces and tabs at the ends of lines:

```sh
pbclean --keep-trailing-whitespace notes.txt
```

The package can also run as a Python module:

```sh
python3 -m pbclean --version
```

### macOS clipboard

Print cleaned clipboard text without changing the clipboard:

```sh
pbclean --clipboard
```

Clean the clipboard and immediately copy the result back:

```sh
pbclean --clipboard --copy
```

You can also send file or standard-input content to the clipboard with
`--copy`. Clipboard options require macOS; file and standard-input cleaning work
wherever Python does.

## Python API

The cleaning function is available for scripts and applications:

```python
from pbclean import clean_text

cleaned = clean_text("Copied\u00a0text\u200b")
assert cleaned == "Copied text"
```

## Development

Clone the project, install it, and run its standard-library test suite:

```sh
git clone https://github.com/ydsveluvolu2996/mac-clipboard-cleaner.git
cd mac-clipboard-cleaner
python3 -m pip install .
python3 -m unittest discover -s tests -v
```

Pull requests are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for the small
project checklist.

## License

[MIT](LICENSE)
