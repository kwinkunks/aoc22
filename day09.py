"""
Advent of Code 2022
Day 9
"""
from typing import Iterable

RAW = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

def parse(data: str) -> Iterable[tuple[str, int]]:
    for row in data.splitlines():
        yield row[0], int(row[1:])

INPUT = list(parse(RAW))


DIRECTIONS = {'R': 1, 'L': -1, 'U': 1j, 'D': -1j}

def sign(n: complex) -> complex:
    r, i = abs(n.real) or 1, abs(n.imag) or 1
    return (n.real / r) + (n.imag / i) * 1j

class Rope:
    def __init__(self, n=2) -> None:
        self.knots = [complex(0, 0) for _ in range(n)]
        self.history = {self.knots[-1]}

    @property
    def head(self) -> complex:
        return self.knots[0]

    @property
    def tail(self) -> complex:
        return self.knots[-1]

    def move(self, direction: str, distance: int) -> 'Rope':
        for _ in range(distance):
            self.knots[0] += DIRECTIONS[direction]
            for i, (u, v) in enumerate(zip(self.knots, self.knots[1:])):
                self.knots[i + 1] = move_knots(u, v)
            self.history.add(self.tail)
        return self

def move_knots(u: complex, v: complex) -> complex:
    """Move knots according to the rules."""
    if (L := abs(u - v)) == 2:
        v += (u - v) / 2
    elif L > 2:
        v = v + sign(u - v)
    return v

def play(data: list[tuple[str, int]], n=2) -> int:
    rope = Rope(n=n)
    for direction, distance in data:
        rope.move(direction, distance)
    return len(rope.history)

assert play(INPUT) == 13 

PART2 = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""

assert play(INPUT, n=10) == 1
assert play(list(parse(PART2)), n=10) == 36


if __name__ == "__main__":

    with open('data/day09.txt') as f:
        moves = list(parse(f.read()))

    part1 = play(moves)
    print('Part 1:', part1)
    assert part1 == 6175

    part2 = play(moves, n=10)
    print('Part 2:', part2)
