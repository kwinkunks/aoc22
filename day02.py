"""
Advent of Code 2022
Day 2
"""
from typing import Callable


RAW = """A Y
B X
C Z"""

def read_input(raw: str) -> list[list[str]]:
    """Parse the input into a list of lists of ints."""
    return [line.split() for line in raw.splitlines()]

TEST = read_input(RAW)


DRAWS_WITH = {'A': 'X', 'B': 'Y', 'C': 'Z'}
BEATEN_BY = {'A': 'Y', 'B': 'Z', 'C': 'X'}
VALUES = {'X': 1, 'Y': 2, 'Z': 3}

def play_one_game(moves: list[str]) -> int:
    """Play a game of rock, paper, scissors."""
    value = VALUES[moves[1]]
    if moves[1] == BEATEN_BY[moves[0]]:
        score =  6
    elif moves[1] == DRAWS_WITH[moves[0]]:
        score = 3
    else:
        score = 0
    return value + score

assert play_one_game(['A', 'Y']) == 8


def play_games(games: list[list[str]], func: Callable[[list[str]], int]) -> int:
    """
    Play all the games.

    Refactored for Part 2 to take a game-playing function.
    """
    return sum(func(g) for g in games)

assert play_games(TEST, play_one_game) == 15


# Hacky way to map each score code letter to its range of scores (indices).
SCORES = '-XXXYYYZZZ'

def play_one_outcome(game: list[str]) -> int:
    """
    Play a game with a fixed outcome.

    Not going to overthink this; just try all the moves until we get the
    required outcome.
    """
    goal_outcome = game[1]
    for move in 'XYZ':
        score = play_one_game([game[0], move])
        if goal_outcome == SCORES[score]:
            return score
    raise ValueError('No move found for outcome', game)

assert play_one_outcome(['A', 'Y']) == 4
assert play_games(TEST, play_one_outcome) == 12


if __name__ == "__main__":
    with open('data/day02.txt') as f:
        games = read_input(f.read())
    part1 = play_games(games, play_one_game)
    print('Part 1:', part1)

    assert part1 == 8933

    part2 = play_games(games, play_one_outcome)
    print('Part 2:', part2)

    assert part2 == 11998
