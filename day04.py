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

def parse(raw: str) -> Iterable:
    """Parse the input."""
    for line in raw.splitlines():
        yield tuple(tuple(map(int, pair.split('-')))
                    for pair in line.split(',')
                    )

TEST = list(parse(RAW))


def contains(pair: tuple[tuple[int, int]]) -> bool:
    """Decide if one range contains the other."""
    a, b = sorted(pair, key=lambda t: t[1] - t[0])
    return b[0] <= a[0] and b[1] >= a[1]

assert sum(contains(pair) for pair in TEST) == 2


def overlaps(pair: tuple[tuple[int, int]]) -> bool:
    """Decide if two ranges overlap."""
    a, b = sorted(pair)
    return b[0] <= a[1]

assert sum(overlaps(pair) for pair in TEST) == 4


if __name__ == "__main__":

    with open('data/day04.txt') as f:
        data = list(parse(f.read()))

    part1 = sum(contains(pair) for pair in data)
    print('Part 1:', part1)
    assert part1 == 562

    part2 = sum(overlaps(pair) for pair in data)
    print('Part 2:', part2)
    assert part2 == 924
