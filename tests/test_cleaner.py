import unittest

from pbclean import clean_text


class CleanTextTests(unittest.TestCase):
    def test_normalizes_line_endings(self) -> None:
        self.assertEqual(clean_text("first\r\nsecond\rthird"), "first\nsecond\nthird")

    def test_replaces_non_breaking_spaces(self) -> None:
        self.assertEqual(clean_text("one\u00a0two\u202fthree"), "one two three")

    def test_removes_invisible_characters(self) -> None:
        source = "\ufeffA\u200bB\u200cC\u200dD\u2060E"
        self.assertEqual(clean_text(source), "ABCDE")

    def test_trims_trailing_spaces_and_tabs(self) -> None:
        self.assertEqual(clean_text("one  \n two\t\n"), "one\n two\n")

    def test_can_preserve_trailing_whitespace(self) -> None:
        self.assertEqual(
            clean_text("one  \n", trim_trailing_whitespace=False),
            "one  \n",
        )


if __name__ == "__main__":
    unittest.main()
