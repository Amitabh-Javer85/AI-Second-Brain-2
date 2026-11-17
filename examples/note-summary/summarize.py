"""Summarize local notes labeled by category."""

import argparse
from collections import Counter
from pathlib import Path


def parse_notes(text: str) -> list[tuple[str, str]]:
    notes = []
    for line_number, line in enumerate(text.splitlines(), start=1):
        if not line.strip():
            continue
        category, _, note = line.partition(":")
        if not category.strip() or not note.strip():
            raise ValueError(f"Line {line_number} must contain a category and note.")
        notes.append((category.strip(), note.strip()))
    return notes


def format_summary(notes: list[tuple[str, str]]) -> str:
    counts = Counter(category for category, _ in notes)
    return "\n".join(
        [f"Total notes: {len(notes)}"]
        + [f"{category}: {count}" for category, count in sorted(counts.items())]
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    try:
        notes = parse_notes(args.input.read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        parser.error(str(error))
    print(format_summary(notes))


if __name__ == "__main__":
    main()
