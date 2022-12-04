# aoc22

It's [Advent of Code 2022](https://adventofcode.com/). No funny business this year, just no frills Python 3.11. Okay, maybe NumPy in an emergency. And I'm using type hints with more deliberation than I usually do, including running MyPy.


## Diary

- Day 1 &mdash; Calorie counting &mdash; the usual kind of warmup, with the only real issue being parsing the 'paragraph'-style input. For the main task, I initially had a silly function simply taking the max, then refactored to sum the top `n` elves.
- Day 2 &mdash; Rock paper scissors &mdash; slightly fiddly RPS game, but the non-overlapping scores allow a hacky approach to Part 2, which essentially wants the inverse problem: the move corresponding to a given outcome. Used [GitHub Codespaces](https://github.com/features/codespaces) for the first time.
- Day 3 &mdash; Rucksack reorganization &mdash; straightforward little bit of set theory. I thought it was heading for something more combinatorial in part 2 (like the rucksacks being out of order) but it's only day 3 I guess. Gotcha: missed that I was throwing newlines into all the strings when reading the data.
- Day 4 &mdash; Camp cleanup &mdash; binary range predicates, reminded me of writing ['striplog'](https://github.com/agilescientific/striplog/blob/main/striplog/interval.py#L316-L335), but took it rather literally and didn't solve it elegantly. Occurred to me that a set theory approach might be nicer, so did it again and I think I prefer it.


## Things I learned about

- [GitHub Codespaces](https://github.com/features/codespaces) is pretty cool
- [PEP 585](https://peps.python.org/pep-0585/) and type hinting since Python 3.9


## Previous years

[2021](https://github.com/kwinkunks/aoc21)  |  [2020](https://github.com/kwinkunks/aoc20)  |  [2019](https://github.com/kwinkunks/aoc19)  |  [2018](https://github.com/kwinkunks/aoc18)
