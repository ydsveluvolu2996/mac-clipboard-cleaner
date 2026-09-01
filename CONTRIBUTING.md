# Contributing

Thanks for improving `mac-clipboard-cleaner`. Small, focused pull requests are
especially welcome.

## Set up the project

```sh
git clone https://github.com/ydsveluvolu2996/mac-clipboard-cleaner.git
cd mac-clipboard-cleaner
python3 -m venv .venv
source .venv/bin/activate
python -m pip install .
python -m unittest discover -s tests -v
```

The project intentionally has no runtime dependencies. Please discuss a new
dependency in an issue before adding one.

## Pull-request checklist

- Keep the change narrow and explain the user-facing behavior.
- Add or update tests when behavior changes.
- Run the full test suite on your branch.
- Update the README when a command or option changes.
- Use a coauthor trailer only when that person genuinely contributed and has
  agreed to be credited.

Bug reports should include the command used, expected output, actual output,
macOS and Python versions, and a minimal sample with sensitive text removed.
