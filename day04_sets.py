"""
Advent of Code 2022
Day 4
"""
from typing import Iterable


RAW = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

def parse(raw) -> Iterable:
    """Parse the input."""
    for line in raw.splitlines():
        ranges = [tuple(map(int, p.split('-'))) for p in line.split(',')]
        yield tuple(set(range(rng[0], rng[1] + 1)) for rng in ranges)

TEST = list(parse(RAW))


def contains(a, b) -> bool:
    """Decide if one range contains the other."""
    return a.issubset(b) or b.issubset(a)

assert sum(contains(*pair) for pair in TEST) == 2


def overlaps(a, b) -> bool:
    """Decide if two ranges overlap."""
    return bool(set.intersection(a, b))

assert sum(overlaps(*pair) for pair in TEST) == 4


if __name__ == "__main__":

    with open('data/day04.txt') as f:
        data = list(parse(f.read()))
    part1 = sum(contains(*pair) for pair in data)
    print('Part 1:', part1)
    assert part1 == 562

    part2 = sum(overlaps(*pair) for pair in data)
    print('Part 2:', part2)
    assert part2 == 924
