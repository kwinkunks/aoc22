import re

RAW = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""


def parse(raw: str) -> list[list[int]]:
    """Read the data and send back lists of sensor and beacon coordinates."""
    pattern = re.compile(r'x=([-0-9]+), y=([-0-9]+): closest beacon is at x=([-0-9]+), y=([-0-9]+)')
    return [list(map(int, i)) for i in pattern.findall(raw)]

def sweep(sensors: list[list[int]], row: int) -> set[int]:
    """Return the set of columns that are swept by the sensors at the given row."""
    # Make a set from the points that got swept.
    swept = set()
    for sx, sy, bx, by in sensors:
        radius = abs(sx - bx) + abs(sy - by)  # L1 space.
        delta = (2 * (radius - abs(sy - row)) + 1) // 2
        for i in range(sx-delta, sx+delta + 1):
            swept.add(i)

    # Remove receivers and maybe sensors from the results.
    for sx, sy, bx, by in sensors:
        if by == row:
            swept.discard(bx)

    return swept

assert len(sweep(parse(RAW), 10)) == 26

if __name__ == '__main__':

    with open('data/day15.txt') as f:
        print(len(sweep(parse(f.read()), 2_000_000)))
