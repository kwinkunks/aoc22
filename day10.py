"""
Advent of Code 2022
Day 10
"""
from typing import Generator, Iterable

RAW = """noop
addx 3
addx -5"""

def parse(stream: str) -> Generator:
    """Read the input stream and return a list of operations."""
    for line in stream.splitlines():
        op, *args = line.split()
        if not args:
            args = ['0']
        yield op, int(*args)

OPS = {'noop': lambda x, n: x, 'addx': lambda x, n: x + n}
CYCLES = {'noop': 1, 'addx': 2}

def execute(operations: list[tuple[str, int]]) -> Generator:
    """Execute the operations and yield (cycle, register) pairs."""
    register = 1
    cycle = 1
    for op, arg in operations:
        for cyc in range(CYCLES[op]):
            cycle += 1
            yield cycle, register
            if cyc == CYCLES[op] - 1:
                continue
            register = OPS[op](register, arg)

def peek(operations: list[tuple[str, int]], peeks: Iterable[int]) -> list[int]:
    """Return the transformed values of the register at the given cycles."""
    captured = []
    for cycle, register in execute(operations):
        if cycle in peeks:
            captured.append(cycle * register)
    return captured

with open('data/day10_test.txt') as f:
    operations = list(parse(f.read()))
    peeks = range(20, 221, 40)
    captured = peek(operations, peeks)
    assert sum(captured) == 13_140


def scan(ops: list[tuple[str, int]]) -> str:
    """Scan the pixels on the screen, lighting the required pixels."""
    screen = '#'
    for pixel, (_, x) in zip(range(1, 240), execute(ops)):
        screen += '#' if abs(pixel % 40 - x) <= 1 else '.'
    for row in [screen[i:i+40] for i in range(0, len(screen), 40)]:
        print(row)
    return screen


with open('data/day10_test.txt') as f:
    operations = list(parse(f.read()))
    print("Test:")
    scan(operations)
    print()


if __name__ == "__main__":

    with open('data/day10.txt') as f:
        operations = list(parse(f.read()))
        peeks = range(20, 221, 40)
        captured = peek(operations, peeks)
        print("Part 1:", sum(captured))

        print("Part 2:")
        scan(operations)
