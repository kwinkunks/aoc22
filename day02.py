from typing import List
from collections import Counter

RAW = """A Y
B X
C Z"""

def read_input(raw: str) -> List[List[str]]:
    """Parse the input into a list of lists of ints."""
    return [r.split() for r in raw.splitlines()]

TEST = read_input(RAW)


DRAWS_WITH = {'A': 'X', 'B': 'Y', 'C': 'Z'}
BEATEN_BY = {'A': 'Y', 'B': 'Z', 'C': 'X'}
VALUES = {'X': 1, 'Y': 2, 'Z': 3}

def one_game(moves: List[str]) -> int:
    v = VALUES[moves[1]]
    if moves[1] == BEATEN_BY[moves[0]]:
        s =  6
    elif moves[1] == DRAWS_WITH[moves[0]]:
        s = 3
    else:
        s = 0
    return v + s

assert one_game(['A', 'Y']) == 8


def play_games(games: List[List[str]]) -> int:
    return sum(one_game(g) for g in games)

assert play_games(TEST) == 15


if __name__ == "__main__":
    with open('data/day02.txt') as f:
        games = read_input(f.read())
    print('Part 1:', play_games(games))
