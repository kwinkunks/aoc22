"""
Advent of Code 2022
Day 8
"""
RAW = """30373
25512
65332
33549
35390"""

def parse(raw) -> list:
    """Parse the input."""
    return [[int(n) for n in row]
            for row in raw.splitlines()]

INPUT = parse(RAW)


def rotate(grid):
    """Rotate grid 90 degrees clockwise."""
    rot = list(zip(*reversed(grid)))
    return [list(row) for row in rot]

def get_visible_dir(grid):
    vis_map = [[1] for row in grid]
    for row, vis_row in zip(grid, vis_map):
        for i, (u, v) in enumerate(zip(row, row[1:])):
            highest = 0
            if v > u and v > highest:
                vis_row.append(1)
                highest = v
            elif v == u and v > highest:
                vis_row.append(0)  # Can't see but doesn't block.
                v = highest
            elif v > highest:
                vis_row.append(1)
                highest = v
            else:
                vis_row.append(0)
                # Blocks: zero the rest of the row.
                for _ in range(len(row) - i - 2):
                    vis_row.append(0)
                break
    return vis_map

def get_visible(grid):
    vis_map = [[0]*len(grid[0]) for row in grid]
    for _ in 'SENW':
        vis = get_visible_dir(grid)
        for i, row in enumerate(vis):
            for j, v in enumerate(row):
                vis_map[i][j] = vis_map[i][j] or v  # Visible from a direction.
        grid = rotate(grid)
        vis_map = rotate(vis_map)
    return vis_map

def count_visible(grid):
    vis_map = get_visible(grid)
    return sum(sum(row) for row in vis_map)

print(get_visible(INPUT))
assert count_visible(INPUT) == 21


if __name__ == "__main__":

    with open('data/day08.txt') as f:
        data = parse(f.read())

    part1 = count_visible(data)
    print('Part 1:', part1)

    assert part1 > 646
