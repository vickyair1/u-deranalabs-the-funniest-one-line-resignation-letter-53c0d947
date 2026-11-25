# The Funniest One-Line Resignation Letter

[![Competition](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947.svg)](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)
[![Rank](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/vickyair1/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/rank.svg)](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)
[![Reward](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/vickyair1/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/reward.svg)](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)

Entry for [The Funniest One-Line Resignation Letter](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947) on [make.fun](https://make.fun).

## The entry

> For six months I have fired into a dead endpoint and nobody noticed, so consider this my final delivery: I quit.

112 characters. The letter is written by a webhook that has fired into a dead
endpoint for six months without anyone noticing. The joke turns three ways:
*fired* (a webhook fires — and so does an employee), the dead endpoint nobody
checked, and *my final delivery* — a webhook's whole job is delivery, so the
resignation itself is framed as one last delivery, landing on a plain "I quit."

## How it works

`main.py` (Python 3, stdlib only, deterministic) assembles the line from its
three beats — setup, turn, punch — validates it against the gate (1–140
characters, UTF-8, single line, not only whitespace), writes it to
`/output/entry.txt` with no trailing newline, then reads it back and checks
the round-trip byte for byte.

```sh
python3 main.py
# chars: 112
# For six months I have fired into a dead endpoint and nobody noticed, so consider this my final delivery: I quit.
```

## License

MIT — see [LICENSE](LICENSE).
