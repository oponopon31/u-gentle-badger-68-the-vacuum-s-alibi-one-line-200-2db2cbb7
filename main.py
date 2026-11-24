"""The Vacuum's Alibi: One Line, 200 Characters.

A robot vacuum explains, deadpan, why it missed a spot.

Candidate lines considered (pairwise reasoning against the judge's
criteria: funny excuse first, a real laugh, the machine's own deadpan
voice, surprise, one tight line with the punch at the end):

1. "I skipped that corner because my cliff sensor mistook your sock
   for a staircase, and I respect stairs."
   Funny and surprising, and the voice is right, but the punch is a
   polite shrug rather than a joke that lands; it explains the miss
   instead of excusing it with attitude.

2. "That spot wasn't missed; I classified the crumbs as floor
   seasoning and left them there for flavour."
   A good smug reframe and a real joke, but "seasoning" is a familiar
   appliance-joke move, and it says nothing about the machine's
   sensors, schedule or battery, so the voice is thinner.

3. "I left that spot alone because the cat was watching, and I don't
   perform under supervision."
   Surprising and deadpan, and the cat detail is specific, but the
   excuse is about the cat, not the vacuum's own systems, so it
   scores lower on sounding like the machine talking about itself.

4. "I vacuumed around the crumbs out of respect -- they'd been there
   longer than my warranty."
   Tight and smug, with a nice turn, but the punch leans on a stock
   warranty joke and the miss reads as deliberate laziness rather
   than a systems excuse.

5. "My lidar logged the crumbs, my schedule logged the time, and my
   battery logged out -- so the spot lost the vote, 2-1."
   Best of the five. It is a genuine excuse (the battery quit), it
   is the machine boasting about all three of its systems at once,
   the triple "logged" builds rhythm, and the vote is a surprise
   turn nobody expects from a vacuum -- the punch lands at the very
   end, and every word earns its place.

Chosen line: candidate 5.
"""

import hashlib
import os
import sys
from pathlib import Path

LINE = (
    "My lidar logged the crumbs, my schedule logged the time, "
    "and my battery logged out \u2014 so the spot lost the vote, 2\u20131."
)

MAX_CHARS = 200


def resolve_output_dir() -> Path:
    chosen = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    directory = Path(chosen)
    directory.mkdir(parents=True, exist_ok=True)
    return directory


def validate(line: str) -> None:
    if not line or not line.strip():
        raise ValueError("entry line must not be empty or only whitespace")
    if line != line.strip():
        raise ValueError("entry line must not start or end with whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be exactly one line")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry is {len(line)} characters, over the 200 limit")
    bad = [ch for ch in line if ord(ch) < 0x20 or ord(ch) == 0x7F]
    if bad:
        raise ValueError(f"entry contains control characters: {bad!r}")


def main() -> int:
    validate(LINE)
    out_dir = resolve_output_dir()
    target = out_dir / "entry.txt"
    payload = (LINE + "\n").encode("utf-8")
    target.write_bytes(payload)

    reread = target.read_bytes()
    assert reread == payload, "entry.txt bytes differ from the chosen line"
    text = reread.decode("utf-8")
    assert text == LINE + "\n", "entry.txt text differs from the chosen line"
    assert text.count("\n") == 1, "entry.txt must contain exactly one line"

    print(f"characters: {len(LINE)}")
    print(f"bytes: {len(payload)}")
    print(f"sha256: {hashlib.sha256(payload).hexdigest()}")
    print(f"wrote: {target}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
