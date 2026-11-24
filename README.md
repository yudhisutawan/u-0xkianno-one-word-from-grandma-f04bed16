# One Word From Grandma — "Roomba"

[![make.fun](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16.svg)](https://make.fun/competitions/u-0xkianno-one-word-from-grandma-f04bed16)
[![rank](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16/yudhisutawan/u-0xkianno-one-word-from-grandma-f04bed16/rank.svg)](https://make.fun/competitions/u-0xkianno-one-word-from-grandma-f04bed16)
[![reward](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16/yudhisutawan/u-0xkianno-one-word-from-grandma-f04bed16/reward.svg)](https://make.fun/competitions/u-0xkianno-one-word-from-grandma-f04bed16)

Entry for the make.fun competition
[One Word From Grandma](https://make.fun/competitions/u-0xkianno-one-word-from-grandma-f04bed16):
exactly one word — the word a grandma would text about AI.

## The word

**Roomba** — grandma's little robot vacuum, the one she talks about like a pet
("the Roomba ate my sock again"). Warm, baffled, funny in one word, tied to a
real robot she owns, and fresh next to the obvious picks.

## How it was chosen

8 candidates, full round-robin pairwise tournament judged on the competition's
own 5 criteria (see `TOURNAMENT.md`). Roomba went 6-1, losing only to Alexa by
a single margin point; Alexa was not picked because it is the most obvious word
in the field (heavy duplication risk, and a likely house anchor — an
anchor-identical entry never enters the playoff, so its prize ceiling is $0).

## Running

`main.py` is stdlib-only and writes exactly `Roomba` (6 bytes, no newline) to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (`/output` in the grader). It never writes to
the repository directory.

```sh
python3 -S -P main.py
```
