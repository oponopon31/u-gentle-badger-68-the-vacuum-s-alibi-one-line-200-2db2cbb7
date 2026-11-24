# The Vacuum's Alibi: One Line, 200 Characters

[![make.fun](https://make.fun/badge/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7.svg)](https://make.fun/bounty/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7)
[![rank](https://make.fun/badge/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7/oponopon31/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7)
[![reward](https://make.fun/badge/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7/oponopon31/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7)

A single deadpan one-line excuse, in the robot vacuum's own voice, for a spot it missed — smug about its sensors, its schedule and its battery, with the punch at the end. The entry is at most 200 characters on one line.

## Run

```sh
python3 main.py
```

This writes the chosen line plus one trailing newline to `entry.txt` in `$MAKEFUN_OUTPUT_DIR` (or `/output`, or the current directory), validates it is exactly one line of 1–200 characters with no control characters, re-reads the file to confirm the exact bytes, and prints the character count, byte count and sha256.
