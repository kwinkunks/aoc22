"""
Advent of Code 2022
Day 11
"""
from dataclasses import dataclass
from typing import Callable, Iterator, Optional, Any

OPS = {
    '*' : lambda x, y: x * y,
    '+' : lambda x, y: x + y,
    '-' : lambda x, y: x - y,
    '/' : lambda x, y: x / y,
}

@dataclass
class Monkey:
    items: list
    op: str
    operand: int
    test: int
    true: int
    false: int
    history: int = 0

    def inspect(self, update: Callable) -> tuple[Optional[int], Optional[int]]:
        if not self.items:
            return None, None
        holding = self.items.pop()
        self.history += 1
        operand = holding if self.operand == 'x' else self.operand
        worry = OPS[self.op](holding, operand)
        if (w := update(worry)) % self.test == 0:
            return w, self.true
        else:
            return w, self.false


def play(monkeys: list, rounds: int, update: Callable) -> list[Monkey]:
    """Play the game."""
    factor = 1
    for f in [m.test for m in monkeys]:
        factor *= f
    for _ in range(rounds):
        for monkey in monkeys:
            while monkey.items:
                worry, target = monkey.inspect(update)
                if worry is not None:
                    monkeys[target].items.append(worry)
        # Adjust the items with common factor.
        for monkey in monkeys:
            monkey.items = [i % factor for i in monkey.items]
    return monkeys

def monkey_business(monkeys: list[Monkey]) -> int:
    """Find the resulting product of the two largest."""
    counts = sorted([m.history for m in monkeys])
    return counts[-2] * counts[-1]

def parse(raw: str) -> Monkey:
    """Parse the raw data into a list of instructions."""
    this: list[Any] = []
    for line in raw.splitlines():
        if line.startswith('  Starting items:'):
            this.append([int(i) for i in line.split(':')[1].split(',')][::-1])
        elif line.startswith('  Operation:'):
            this.append(line.split(':')[1].split()[-2])
            try:
                this.append(int(line.split()[-1]))
            except ValueError:
                this.append('x')
        elif line.startswith('  Test:'):
            this.append(int(line.split()[-1]))
        elif line.strip().startswith('If true:'):
            this.append(int(line.split()[-1]))
        elif line.strip().startswith('If false:'):
            this.append(int(line.split()[-1]))
    return Monkey(*this)

def read_file(raw:str) -> Iterator[Monkey]:
    for text in raw.split('\n\n'):
        yield parse(text)

def main(fname: str, update: Callable, rounds: int=20) -> int:
    """Main function."""
    with open(fname) as f:
        monkeys = list(read_file(f.read()))
        monkeys = play(monkeys, rounds=rounds, update=update)
    return monkey_business(monkeys)


if __name__ == "__main__":
    assert main('data/day11_test.txt', lambda x: x // 3) == 10605
    part1 = main('data/day11.txt', lambda x: x // 3)
    print('Part 1', part1)
    assert part1 == 58322

    assert main('data/day11_test.txt', rounds=10_000, update=lambda x: x) == 2713310158
    part2 = main('data/day11.txt', rounds=10_000, update=lambda x: x)
    print("Part 2", part2)
