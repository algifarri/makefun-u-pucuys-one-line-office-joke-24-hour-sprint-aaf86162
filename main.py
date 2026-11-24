#!/usr/bin/env python3
"""One-Line Office Joke: 24-Hour Sprint entry.

Writes one one-line office joke to /output/entry.txt (UTF-8, 1-200
characters, inside the gate). Deterministic, standard library only,
no network, no environment reads.

The line (150 characters): "Our standup was supposed to be fifteen
minutes, so naturally it now has its own agenda, its own follow-up
meeting, and a small family in the calendar." The setup is a ritual
every office worker knows, the fifteen-minute standup; the turn is
that the meeting has reproduced, gaining an agenda, a follow-up
meeting of its own, and finally a family living in the calendar.
One specific detail, one escalation, punchline on the last words.
The calendar is the office's real memory, so a family living in it
is the natural end of a meeting that never ends.
"""

import os

TEXT = (
    "Our standup was supposed to be fifteen minutes, so naturally "
    "it now has its own agenda, its own follow-up meeting, and a "
    "small family in the calendar."
)


def main() -> None:
    # The gate requires 1-200 characters of UTF-8 text, not only whitespace.
    assert 1 <= len(TEXT) <= 200, "entry must be 1-200 characters"
    assert TEXT.strip() == TEXT, "entry must not start or end with whitespace"
    assert "\n" not in TEXT, "entry must be exactly one line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(TEXT)


if __name__ == "__main__":
    main()
