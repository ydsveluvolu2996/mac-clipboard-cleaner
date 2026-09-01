import subprocess
import unittest
from unittest.mock import patch

from pbclean.clipboard import ClipboardError, copy_to_clipboard, read_clipboard


class ClipboardTests(unittest.TestCase):
    @patch("pbclean.clipboard.subprocess.run")
    def test_reads_clipboard_text(self, run) -> None:
        run.return_value = subprocess.CompletedProcess(["pbpaste"], 0, "copied text", "")

        self.assertEqual(read_clipboard(), "copied text")
        run.assert_called_once_with(
            ["pbpaste"],
            check=True,
            capture_output=True,
            encoding="utf-8",
            text=True,
        )

    @patch("pbclean.clipboard.subprocess.run")
    def test_copies_text_to_clipboard(self, run) -> None:
        copy_to_clipboard("clean text")

        run.assert_called_once_with(
            ["pbcopy"],
            check=True,
            input="clean text",
            capture_output=True,
            encoding="utf-8",
            text=True,
        )

    @patch("pbclean.clipboard.subprocess.run", side_effect=FileNotFoundError)
    def test_reports_missing_clipboard_command(self, run) -> None:
        with self.assertRaisesRegex(ClipboardError, "requires macOS"):
            read_clipboard()


if __name__ == "__main__":
    unittest.main()
