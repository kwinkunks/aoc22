# aoc22

It's [Advent of Code 2022](https://adventofcode.com/). No funny business this year, just no frills Python 3.11. Okay, maybe NumPy in an emergency. And I'm using type hints with more deliberation than I usually do, including running MyPy.


## Diary

⚠️ **Contains spoilers!**

- [Day 1](day01.py) &mdash; Calorie Counting &mdash; the usual kind of warmup, with the only real issue being parsing the 'paragraph'-style input. For the main task, I initially had a silly function simply taking the max, then refactored to sum the top `n` elves.
- [Day 2](day02.py) &mdash; Rock Paper Scissors &mdash; slightly fiddly RPS game, but the non-overlapping scores allow a hacky approach to Part 2, which essentially wants the inverse problem: the move corresponding to a given outcome. Used [GitHub Codespaces](https://github.com/features/codespaces) for the first time. Indirectly learned about enums from [Joel Grus](https://www.youtube.com/watch?v=Tbm4ycpq2ic).
- [Day 3](day03.py) &mdash; Rucksack Reorganization &mdash; straightforward little bit of set theory. I thought it was heading for something more combinatorial in part 2 (like the rucksacks being out of order) but it's only day 3 I guess. Gotcha: missed that I was throwing newlines into all the strings when reading the data. Reminded later in a YouTube comment of [string.ascii_letters](https://docs.python.org/3/library/string.html#string.ascii_letters) which would be a nice way to score.
- [Day 4](day04.py) &mdash; Camp Cleanup &mdash; binary range predicates, reminded me of writing ['striplog'](https://github.com/agilescientific/striplog/blob/main/striplog/interval.py#L316-L335), but took it rather literally and didn't solve it elegantly. Occurred to me that a set theory approach might be nicer, so did it again and I think I prefer it. Realizing that I almost never use classes for these things; will try to practice that, if I remember.
- [Day 5](day05.py) &mdash; Supply Stacks &mdash; reading the input data was fiddly, but the challenge itself was not hard... although I caught myself out briefly in Part 2 with unwanted mutation of the `stacks` in Part 1. Initially solved with separate functions but then refactored.
- [Day 6](day06.py) &mdash; Tuning Trouble &mdash; maybe the easiest day so far, which bodes ill for tomorrow. Called for comparing sequences of characters, which I always do with `zip`. Maybe there's something better in `itertools`. Wonder if we'll see these sequences again? So much for using classes more, maybe it's true what they say about OOP...
- [Day 7](day07.py) &mdash; No Space Left on Device &mdash; trees, my nemesis. Nemesises. Anyway, reverse engineering a directory tree from a command line session sounds quite tricky, but I got away with accumulating the file sizes only. Thought it might bite me in part 2, but no. Caught myself out by treating directory names as unique, which works on the sample but not on the real input.
- [Day 8](day08.py) &mdash; Treetop Tree House &mdash; the first grid of the year, always fun. Thought about 1st or 2nd derivatives for a minute, and not obvious how to do it with convolution, settled on brute force. Instead of fiddling with directions, I'm just doing the analysis from left to right and rotating the grid 4 times. Found the visibility logic a bit fiddly, but got there in the end.
- [Day 9](day09.py) &mdash; Rope Bridge &mdash; coordinates and vectors! Which I usually enjoy... Part 1 was fine, fun even. Part 2 was a headache, utterly self-inflicted: I was applying the head update to every knot, as well as applying the 'follow previous knot' rule, but it took a ridiculous amount of time to see this. Sigh. Pleased with the tercity of the result though, and with a class too!
- [Day 10](day10.py) &mdash; Cathode-Ray Tube &mdash; argh, it's the compiler, though I always enjoy the graphical solutions. Nearly got distracted by the fiddly timing rules, but in the end it was fine. Not pretty, I'm sure... if this thing comes back maybe we can clean up a bit. Side-note: quite enjoying using generators more often, though probably not idiomatically.
- [Day 11](day11.py) &mdash; Monkey in the Middle &mdash; surprisingly enjoyable modulo arithmetic / number theory problem. Got a bit obsessed with the idea that the exponential monkey should be controlled (if prime p divides a<sup>2</sup> then it divides a) but then picked up on the "find another way to manage your worry level" clue.
- [Day 12](day12.py) &mdash; my first time trying to implement A*. Once again, my almost-solution solves the example but not the real input. I think I'm missing something to do with the criterion for updating the cost at a given target. I'll finish it some day...
- [Day 15](day15.py) &mdash; was fun, at first. I solved part 1 fairly easily, as the first thing I tried worked. Part 2 works perfectly on the test, but something is breaking on the real input data and since my non-working solution is very slow (I'm finding where the border-squares of the L1 'circles' overlap) I assume it's the wrong approach.

I seem to have fallen off the wagon and am busy with other things now, so I think this is the end of the line for me this year. Fun times, as always :)


## Things I learned about

- [GitHub Codespaces](https://github.com/features/codespaces) is pretty cool.
- [PEP 585](https://peps.python.org/pep-0585/) and type hinting since Python 3.9, incl.uding lots of new (to me) syntax
- [Enums](https://docs.python.org/3/library/enum.html) from watching [Joel Grus's solution](https://www.youtube.com/watch?v=Tbm4ycpq2ic); never really understood them before.
- Dijkstra and A* were algorithms I'd heard of but never tried to implement, although I've solved AoC puzzles in the past with clunky / brute-force methods where they would have helped. This year I implemented a 'mostly' working A* for Day 12. 


## Previous years

[2021](https://github.com/kwinkunks/aoc21)  |  [2020](https://github.com/kwinkunks/aoc20)  |  [2019](https://github.com/kwinkunks/aoc19)  |  [2018](https://github.com/kwinkunks/aoc18)
