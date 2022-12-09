"""
Advent of Code 2022
Day 9
"""
from typing import Self

RAW = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

def parse(data: str) -> tuple[str, int]:
    for row in data.splitlines():
        yield row[0], int(row[1:])

INPUT = list(parse(RAW))


DIRECTIONS = {'R': 1, 'L': -1, 'U': 1j, 'D': -1j}

def sign(n: complex) -> complex:
    return (n.real / abs(n.real)) + (n.imag / abs(n.imag)) * 1j

class Rope:
    def __init__(self) -> None:
        self.head = complex(0, 0)
        self.tail = complex(0, 0)
        self.history = {self.tail}

    def __repr__(self) -> str:
        return f'Rope(head={self.head}, tail={self.tail})'

    def move(self, direction: str, distance: int) -> Self:
        for _ in range(distance):
            self.head += DIRECTIONS[direction]
            self = self.move_tail()
        return self

    def move_tail(self) -> Self:
        """Move the tail according to the following rules: if the head is
        touching the tail, do nothing; if the head is adjacent to the tail,
        do nothing. If the head is two units away from the tail,
        move the tail one unit closer to the head. If the head is more than two
        units away from the tail, move the tail one diagonal unit closer to
        the head."""
        if (L := abs(self.head - self.tail)) < 2:
            pass
        elif L == 2:
            self.tail += (self.head - self.tail) / 2
        elif L > 2:
            self.tail += sign(self.head - self.tail)
        self.history.add(self.tail)
        return self

def play(data: list[tuple[str, int]]) -> int:
    rope = Rope()
    for direction, distance in data:
        rope.move(direction, distance)
    return len(rope.history)

assert(play(INPUT) == 13)


if __name__ == "__main__":

    with open('data/day09.txt') as f:
        moves = list(parse(f.read()))

    part1 = play(moves)
    print('Part 1:', part1)
    assert part1 == 6175
