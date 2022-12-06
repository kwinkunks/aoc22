"""
Advent of Code 2022
Day 6
"""
RAW = """mjqjpqmgbljsphdztnvjfqwrcgsmlb"""


def first_packet(stream: str, n: int) -> int:
    """
    Find the end position of the first packet of n chars with no repeats.
    """
    group = [stream[i:] for i in range(n)]
    for i, chunk in enumerate(zip(*group)):
        if len(set(chunk)) == n:
            return i + n
    raise ValueError('No packet found')

assert first_packet(RAW, n=4) == 7
assert first_packet(RAW, n=14) == 19


if __name__ == "__main__":

    with open('data/day06.txt') as f:
        stream = f.read()

    part1 = first_packet(stream, n=4)
    print('Part 1:', part1)
    assert part1 == 1042

    part2 = first_packet(stream, n=14)
    print('Part 2:', part2)
