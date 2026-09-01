"""Core text-cleaning behavior."""

import re


_CHARACTER_TRANSLATION = str.maketrans(
    {
        "\u00a0": " ",  # non-breaking space
        "\u202f": " ",  # narrow non-breaking space
        "\u200b": None,  # zero-width space
        "\u200c": None,  # zero-width non-joiner
        "\u200d": None,  # zero-width joiner
        "\u2060": None,  # word joiner
        "\ufeff": None,  # byte-order mark / zero-width no-break space
    }
)


def clean_text(text: str, *, trim_trailing_whitespace: bool = True) -> str:
    """Return a cleaned version of *text* without changing its wording.

    The function normalizes CRLF and CR line endings, converts non-breaking
    spaces to regular spaces, removes common invisible formatting characters,
    and optionally removes spaces and tabs at the ends of lines.
    """

    cleaned = text.replace("\r\n", "\n").replace("\r", "\n")
    cleaned = cleaned.translate(_CHARACTER_TRANSLATION)

    if trim_trailing_whitespace:
        cleaned = "\n".join(
            re.sub(r"[ \t]+$", "", line) for line in cleaned.split("\n")
        )

    return cleaned
