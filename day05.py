"""
Advent of Code 2022
Day 5
"""
from typing import Iterable


RAW = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

def read(raw) -> Iterable:
    """Gross."""
    stacklines, movelines = [text.splitlines() for text in raw.split('\n\n')]
    stacks = ['' for i in range(1, len(stacklines[0]), 4)]
    for i in range(len(stacks)):
        for row in stacklines[:-1]:
            stacks[i] += row[1 + (4*i)]
    
    moves = []
    for row in movelines:
        moves.append(tuple(map(int, row.split()[1::2])))
    return [''] + [s.strip() for s in stacks], moves

def make_moves(stacks, moves, singly=False):
    stacks = stacks.copy()
    for n, fra, til in moves:
        grab = stacks[fra][:n]
        stacks[fra] = stacks[fra][n:]
        stacks[til] = grab[::-1 if singly else 1] + stacks[til]
    return stacks

def get_message(stacks):
        return ''.join(stack[:1] for stack in stacks)

STACKS, MOVES = read(RAW)

assert get_message(make_moves(STACKS, MOVES, singly=True)) == 'CMZ'

assert get_message(make_moves(STACKS, MOVES)) == 'MCD'


if __name__ == "__main__":

    with open('data/day05.txt') as f:
        stacks, moves = read(f.read())

    part1 = get_message(make_moves(stacks, moves, singly=True))
    print('Part 1:', part1)
    assert part1 == 'ZSQVCCJLL'

    part2 = get_message(make_moves(stacks, moves))
    print('Part 2:', part2)
