"""Native macOS clipboard helpers."""

from __future__ import annotations

import subprocess


class ClipboardError(RuntimeError):
    """Raised when a macOS clipboard command cannot be used."""


def read_clipboard() -> str:
    """Return UTF-8 text currently stored on the macOS clipboard."""

    try:
        completed = subprocess.run(
            ["pbpaste"],
            check=True,
            capture_output=True,
            encoding="utf-8",
            text=True,
        )
    except FileNotFoundError as error:
        raise ClipboardError("pbpaste was not found; --clipboard requires macOS") from error
    except (subprocess.CalledProcessError, UnicodeError) as error:
        raise ClipboardError(f"could not read the clipboard: {error}") from error

    return completed.stdout


def copy_to_clipboard(text: str) -> None:
    """Replace the macOS clipboard contents with *text*."""

    try:
        subprocess.run(
            ["pbcopy"],
            check=True,
            input=text,
            capture_output=True,
            encoding="utf-8",
            text=True,
        )
    except FileNotFoundError as error:
        raise ClipboardError("pbcopy was not found; --copy requires macOS") from error
    except (subprocess.CalledProcessError, UnicodeError) as error:
        raise ClipboardError(f"could not update the clipboard: {error}") from error
