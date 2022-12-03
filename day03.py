"""
Advent of Code 2022
Day 3
"""
RAW = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

TEST = RAW.splitlines()


def find_duplicates(rucksack: str) -> set[str]:
    """Returns the priority of items appearing in both compartments."""
    n = len(rucksack)
    comp1, comp2 = rucksack[n//2:], rucksack[:n//2]
    return set(comp1) & set(comp2)

assert find_duplicates(TEST[0]) == {'p'}


def get_priority(item: str) -> int:
    """Returns the priority of an item."""
    return ord(item) - 96 if item.islower() else ord(item) - 64 + 26

assert get_priority('p') == 16

def sum_dupe_priority(rucksacks: list[str]) -> int:
    """Returns the sum of the priorities of items appearing in both compartments."""
    return sum(sum(get_priority(i) for i in find_duplicates(r)) for r in rucksacks)

assert sum_dupe_priority(TEST) == 157


def find_badge(rucksacks: list[str]) -> str:
    """Find the common item in all three rucksacks."""
    assert len(rucksacks) == 3, 'Must be three rucksacks'
    item, = set.intersection(*[set(rucksack) for rucksack in rucksacks])
    return item

def find_badges_in_groups(rucksacks: list[str]) -> list[str]:
    """Find the badge in each group of 3 rucksacks."""
    return [find_badge(rucksacks[i:i+3]) for i in range(0, len(rucksacks), 3)]

assert find_badges_in_groups(TEST) == ['r', 'Z']


if __name__ == "__main__":
    with open('data/day03.txt') as f:
        rucksacks = f.read().splitlines()
    part1 = sum_dupe_priority(rucksacks)
    print('Part 1:', part1)
    assert part1 == 7980

    part2 = sum(get_priority(b) for b in find_badges_in_groups(rucksacks))
    print('Part 2:', part2)
    assert part2 == 2881
