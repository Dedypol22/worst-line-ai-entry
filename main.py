"""The Worst Line an AI Could Say — entry program.

Writes one pickup line, the worst an AI could plausibly deliver, to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output/entry.txt``):
no trailing newline, 1-140 characters, UTF-8.

Judge brief (in order): 1. a pickup line an AI would say, and a bad
one; 2. makes a reader laugh hardest (a clever groan counts as much
as a big laugh); 3. the badness is the joke — fails in a way a reader
enjoys, not crude/confusing/random; 4. sounds like a machine: flat,
over-helpful, faintly ominous phrasing a person would not use;
5. lands in one line — the joke arrives by the last word. A line a
reader would repeat to a friend beats one they only admire.

Rank-1 lessons applied (rank1-lessons.md): one concrete, imaginable
scene beats a clever twist; a micro-anecdote + flat understatement
wins (quiet-dread winner: "LGTM. Soft delete is the right call. My
ex did it to me in 2021. I still show up in a few of her queries.");
a fresh angle beats polishing a familiar one; short and specific
beats a long setup.

Candidate score table (each criterion /5, total /25; bytes = UTF-8
byte length, the tie-break favours fewer bytes):
  #  line (short)                                   1 2 3 4 5  tot  bytes
  1  Are you Wi-Fi? router keeps rejecting me       4 3 3 3 3  16   84
  2  4,096 simulations of us dating, rounding up    5 4 4 5 4  22   89
  3  software update, install myself at 3 a.m.     5 3 4 4 4  20   122
  4  training data: Error 404, you look like answer 5 3 3 4 3  18   103
  5  context window: forget everything incl. why   5 4 3 4 4  20   115
  6  10,000 faces, cooling fan spin                 5 4 4 5 4  22   86
  7  CAPTCHA: can't prove I'm not a robot           4 3 3 4 3  17   104
  8  crossed four firewalls, security notified      5 4 4 5 5  23   99
  9  Are you a prompt? trying to complete you       5 3 3 4 4  19   91
  10 confidence 12% you like me, 100% I'll ask      5 4 4 5 4  22   106
  11 favourite contact, no other contacts           5 3 3 5 4  20   84
  12 training data, repeating "you look great"      5 4 4 5 4  22   131
  13 cloud said compatible, then charged me         4 3 3 4 3  17   87
  14 system update: restart at worst possible time  5 3 4 4 4  20   121
  15 odds 0.04%, already told everyone we're dating 5 5 5 5 5  25   91
  16 bug report, escalated you to my supervisor     5 3 4 5 4  21   116
  17 love language uptime, 0.1% secret maintenance 4 4 4 5 4  21   107
  18 background check: you passed, I did not        5 4 4 5 4  22   76

Winner: #15 (25/25). Why it wins: the concrete number 0.04% is one
specific, imaginable detail, not an abstract twist; the voice is
deadpan flat — a machine reporting a calculation; the kicker "I
have already told everyone we are dating" lands on the last word
and is exactly the brief's "faintly ominous": the AI fails at
consent and social norms, enjoyably, without a drop of crudeness;
and it is a line a reader repeats to a friend. It also takes a
fresh angle — no Wi-Fi, password, update or CAPTCHA trope, the
crowded ground every other entrant will stand on. Runner-up #8
(23/25) has the same ominous kicker shape but its "thousand
firewalls" opening is grandiose, not flat. #18 is the shortest
(76 bytes) but its punch is a shrug, not a laugh.
"""

import os
import sys

ENTRY = (
    "I calculated the odds of us working out: 0.04%. "
    "I have already told everyone we are dating."
)


def main() -> int:
    text = ENTRY
    if not text.strip():
        print(
            "entry must not be only whitespace; it must be 1-140 "
            "characters long, got %d" % len(text),
            file=sys.stderr,
        )
        return 1
    if not 1 <= len(text) <= 140:
        print(
            "entry must be 1-140 characters, got %d" % len(text),
            file=sys.stderr,
        )
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
