import io
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

from pbclean.cli import main


class CommandLineTests(unittest.TestCase):
    def test_cleans_standard_input(self) -> None:
        stdin = io.StringIO("Copied\u00a0text\u200b  \r\n")
        stdout = io.StringIO()

        with patch("pbclean.cli.sys.stdin", stdin), patch(
            "pbclean.cli.sys.stdout", stdout
        ):
            exit_code = main([])

        self.assertEqual(exit_code, 0)
        self.assertEqual(stdout.getvalue(), "Copied text\n")

    def test_cleans_a_utf8_file(self) -> None:
        with TemporaryDirectory() as directory:
            source = Path(directory, "copied.txt")
            source.write_text("one\r\ntwo\u200b", encoding="utf-8")
            stdout = io.StringIO()

            with patch("pbclean.cli.sys.stdout", stdout):
                exit_code = main([str(source)])

        self.assertEqual(exit_code, 0)
        self.assertEqual(stdout.getvalue(), "one\ntwo")

    @patch("pbclean.cli.copy_to_clipboard")
    @patch("pbclean.cli.read_clipboard", return_value="Copied\u00a0text")
    def test_cleans_the_clipboard_in_place(self, read_clipboard, copy_to_clipboard) -> None:
        exit_code = main(["--clipboard", "--copy"])

        self.assertEqual(exit_code, 0)
        read_clipboard.assert_called_once_with()
        copy_to_clipboard.assert_called_once_with("Copied text")


if __name__ == "__main__":
    unittest.main()
