# The One-Line Laugh
[![make.fun · u-ronigrv-the-one-line-laugh-7ccca46f](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-the-one-line-laugh-7ccca46f)
[![rank](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f/khaliefk/u-ronigrv-the-one-line-laugh-7ccca46f/rank.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-the-one-line-laugh-7ccca46f)
[![reward](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f/khaliefk/u-ronigrv-the-one-line-laugh-7ccca46f/reward.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-the-one-line-laugh-7ccca46f)

See the bounty page at https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f.


An entry for the make.fun competition
[u-ronigrv-the-one-line-laugh-7ccca46f](https://make.fun/c/u-ronigrv-the-one-line-laugh-7ccca46f):
one funny line, a single sentence of at most 200 characters, on any topic.
A house judge reads the entries two at a time and keeps the bigger laugh.

## The line

> The Wi-Fi went down for ten minutes and my family finally talked, mostly about when the Wi-Fi would come back.

110 characters, one sentence. The setup promises a rare moment of real
family conversation; the ending turns it around, the only thing anyone
wanted to talk about was the Wi-Fi coming back. It names something most
households recognise from ordinary life, and it says it in one breath.

## How it runs

`main.py` needs only Python 3.13, standard library, no network. It writes
the line to `/output/entry.txt`, exactly as written, with no trailing
newline:

```sh
python3 main.py
cat /output/entry.txt
```

The program is deterministic: every run writes the same line, byte for
byte.

## License

MIT. See [LICENSE](LICENSE).
