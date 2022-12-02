from typing import List


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
    """Parse the input into a list of lists of ints."""
    return [[int(n) for n in r.split()] for r in raw.split('\n\n')]

TEST = read_input(RAW)


def elf_calories(elves: List[List[int]]) -> List[int]:
    """Sum the snacks for each elf."""
    return [sum(elf) for elf in elves]

def sum_top(numbers: List[int], n: int=1) -> int:
    """Sum the top n numbers. Refactored after Part 2."""
    return sum(sorted(numbers)[-n:])

assert sum_top(elf_calories(TEST)) == 24_000

assert sum_top(elf_calories(TEST), n=3) == 45_000


if __name__ == "__main__":
    with open('data/day01.txt') as f:
        numbers = read_input(f.read())
    print('Part 1:', sum_top(elf_calories(numbers)))
    print('Part 2:', sum_top(elf_calories(numbers), n=3))
