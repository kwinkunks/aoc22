from typing import List
from collections import Counter

RAW = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

def read_input(raw: str) -> List[List[int]]:
    return [[int(n) for n in r.split()] for r in raw.split('\n\n')]

TEST = read_input(RAW)


def elf_calories(elves: List[List[int]]) -> List[int]:
    return [sum(elf) for elf in elves]

def most_calories(numbers: List[int]) -> int:
    return max(numbers)

assert most_calories(elf_calories(TEST)) == 24_000


def top_three(numbers: List[int]) -> int:
    return sum(sorted(numbers)[-3:])

assert top_three(elf_calories(TEST)) == 45_000


if __name__ == "__main__":
    with open('data/day01.txt') as f:
        numbers = read_input(f.read())
    print('Part 1:', most_calories(elf_calories(numbers)))
    print('Part 2:', top_three(elf_calories(numbers)))
