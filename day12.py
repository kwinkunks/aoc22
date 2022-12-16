"""
Advent of Code 2022
Day 12
"""
from functools import total_ordering
from queue import PriorityQueue

RAW = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""

@total_ordering
class Point:
    def __init__(self, row, col):
        self.r = row
        self.c = col
    
    def __repr__(self):
        return f"Point({self.r}, {self.c})"

    def __add__(self, other):
        return Point(self.r + other.r, self.c + other.c)

    def __le__(self, other) -> bool:
        return (self.r, self.c) < (other.r, other.c)

    def __eq__(self, other) -> bool:
        return (self.r, self.c) == (other.r, other.c)

    def __hash__(self):
        return hash(frozenset((self.r, self.c)))

def parse(data: str) -> list[list[int]]:
    start: Point
    goal: Point
    grid: list[list[int]] = []
    for r, row in enumerate(data.splitlines()):
        grid_row: list[int] = []
        for c, char in enumerate(row):
            if char == 'S':
                grid_row.append(0)
                start = Point(r, c)
            elif char == 'E':
                grid_row.append(25)
                goal = Point(r, c)
            else:
                grid_row.append(ord(char) - 97)
        grid.append(grid_row)
    return grid, start, goal

def heuristic(grid: list, a: tuple, goal: tuple):
    """Heuristic function for A* search."""
    diff = 26 - read_grid(grid, a)
    L1 = abs(a.r - goal.r) + abs(a.c - goal.c)
    return L1

def read_grid(grid, loc):
    if loc.r < 0 or loc.c < 0:
        return None
    if loc.r >= len(grid) or loc.c >= len(grid[0]):
        return None
    return grid[loc.r][loc.c]

def get_path(parents, target):
    path = list()
    while (node := parents.get(target)):
        path.append(node)
        target = node
    return path[::-1]


STEPS = [Point(0, 1), Point(0, -1), Point(1, 0), Point(-1, 0)]

def explore(grid, start, goal):
    """Attempt at A*."""
    queue = PriorityQueue()
    queue.put(((0, 0), start))
    visited = {start: 0}
    parents = dict()
    while True:
        _, this = queue.get()
        if this == goal: break
        u = read_grid(grid, this)
        cost = visited[this]
        for step in STEPS:
            target = this + step
            v = read_grid(grid, target)
            if v is None: continue
            if v - u > 1: continue
            next_cost = visited.get(target, 1e12)
            if (g := cost + v - u) >= next_cost: continue
            parents[target] = this
            h = heuristic(grid, this, goal)
            queue.put((g+h, target))
            visited[target] = g  
    print(get_path(parents, target))
    return(len(get_path(parents, target))) 


x = explore(*parse(RAW))
print(x)
assert x == 31


if __name__ == "__main__":

    with open('data/day12.txt') as f:
        data = f.read()

print("Part 1:", explore(*parse(data)))
