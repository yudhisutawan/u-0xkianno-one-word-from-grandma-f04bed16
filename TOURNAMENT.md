# Tournament — One Word From Grandma

Method (per ~/workspace/makefun/win-gap-playbook.md, adapted to one-word
candidates): full round-robin, 28 games. Each game is decided by the judge's
own rule — go through the 5 criteria in order, the first one where the words
differ decides, unless a later one differs by much more. Margin 1 = by a hair,
5 = overwhelming.

## Results (W-L)

| Word | W | L |
|------|---|---|
| Alexa | 7 | 0 |
| **Roomba** | **6** | **1** |
| Contraption | 5 | 2 |
| Doohickey | 4 | 3 |
| Tinman | 3 | 4 |
| Al | 2 | 5 |
| Gizmo | 1 | 6 |
| Beepboop | 0 | 7 |

## Head-to-head log (winner first, margin)

- Alexa > Roomba 1 (C1: Alexa is the AI she talks to; Roomba is "the vacuum")
- Alexa > Contraption 1, Alexa > Doohickey 2, Alexa > Gizmo 2, Alexa > Al 2,
  Alexa > Beepboop 3, Alexa > Tinman 2
- Roomba > Contraption 2 (C4: real robot she owns vs generic machine word)
- Roomba > Doohickey 1, Roomba > Gizmo 1, Roomba > Al 1, Roomba > Beepboop 2,
  Roomba > Tinman 1
- Contraption > Doohickey 1, Contraption > Gizmo 1, Contraption > Al 1,
  Contraption > Beepboop 2, Contraption > Tinman 1
- Doohickey > Gizmo 1 (C2), Doohickey > Al 1 (C2), Doohickey > Beepboop 1,
  Doohickey > Tinman 1 (C2)
- Tinman > Gizmo 1 (C3), Tinman > Al 1 (C4), Tinman > Beepboop 1
- Al > Gizmo 1 (C3), Al > Beepboop 1
- Gizmo > Beepboop 1

## Final pick: Roomba (not the round-robin winner Alexa)

Alexa won the round-robin 7-0, but its only edge over Roomba is margin 1 on
criterion 1 — a hair. Two field factors the pairwise games cannot see overturn
that hair:

1. **Duplication / anchor risk.** Alexa is the single most obvious word in
   this competition; hundreds of entries are likely to submit it or Siri, and
   an obvious word is a likely house anchor. An entry byte-identical to a
   fixed house text shares its rate and **never enters the playoff**, so its
   prize ceiling is $0. Roomba is specific enough to be near-zero anchor risk.
2. **Freshness (criterion 5).** Roomba beats Alexa clearly (4 vs 2) — the
   judge's own criterion 5, and the one that separates a top-10 word from the
   crowd in a field of thousands.

Roomba is not a weak compromise: it went 6-1, winning every game except the
margin-1 loss to Alexa, and it wins criteria 2, 3 and 5 outright against the
field. Verdict: **Roomba**.

## Gate check

`main.py` writes exactly `Roomba` (6 bytes, no trailing newline) to
`$MAKEFUN_OUTPUT_DIR/entry.txt`. Verified with `python3 -S -P main.py`
(stdlib-only simulation, no site-packages): exit 0, output byte-identical,
repository directory untouched.
