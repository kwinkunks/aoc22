"""
Advent of Code 2022
Day 9
"""
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
    def __init__(self, n=2) -> None:
        self.knots = [complex(0, 0) for _ in range(n)]
        self.history = {self.knots[-1]}

    def __repr__(self) -> str:
        return f'Rope(head={self.head}, tail={self.tail})'

    @property
    def head(self) -> complex:
        return self.knots[0]

    @property
    def tail(self) -> complex:
        return self.knots[-1]

    def move(self, direction: str, distance: int):
        for _ in range(distance):
            knots = self.knots.copy()
            for i, (u, v) in enumerate(zip(knots, knots[1:])):
                u_, v_ = move_knots(u, v, direction)
                knots[i], knots[i+1] = u_, v_
            self.knots = knots
            self.history.add(self.tail)
        return self

def move_knots(u, v, direction: str):
    """Move knot v according to the rules."""
    if (L := abs(u - v)) == 2:
        v += (u - v) / 2
    elif L > 2:
        v += sign(u - v)
    return u + DIRECTIONS[direction], v

def play(data: list[tuple[str, int]], n=2) -> int:
    rope = Rope(n=n)
    for direction, distance in data:
        rope.move(direction, distance)
        print(rope)
    return len(rope.history)

# assert(play(INPUT) == 13)

print("length 10: ", play(INPUT, n=10))

PART2 = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""

# print(play(list(parse(PART2)), n=10))
# assert play(list(parse(PART2)), n=10) == 36


if __name__ == "__main__":

    with open('data/day09.txt') as f:
        moves = list(parse(f.read()))

    # part1 = play(moves)
    # print('Part 1:', part1)
    # assert part1 == 6175
