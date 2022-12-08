"""
Advent of Code 2022
Day 8
"""
RAW = """30373
25512
65332
33549
35390"""

def parse(raw: str) -> list:
    """Parse the input."""
    return [[int(n) for n in row]
            for row in raw.splitlines()]

INPUT = parse(RAW)


def rotate(grid: list[list[int]]) -> list[list[int]]:
    """Rotate grid 90 degrees."""
    rot = list(zip(*reversed(grid)))
    return [list(row) for row in rot]

def get_visible_row(row: list[int], vis_row: list[int], x: int=0) -> list[int]:
    """Get the visible trees in a row, starting at position x.
    Using visibility rules from part 2.
    """
    for v in row[x+1:]:
        vis_row.append(1)
        if v >= row[x]:
            break
    return vis_row

def get_visible_dir(grid: list[list[int]]) -> list[list[int]]:
    """Get the trees visible from the left."""
    vis_map = [[1] for row in grid]
    for row, vis_row in zip(grid, vis_map):
        highest = row[0]
        for u, v in zip(row, row[1:]):
            if v > u and v > highest:
                vis_row.append(1)
                highest = v
            elif v == u and v > highest:
                vis_row.append(0)  # Can't see but doesn't block.
                highest = v
            else:
                vis_row.append(0)
    return vis_map

def get_visible(grid: list[list[int]]) -> list[list[int]]:
    """Get visible trees from each direction and OR them."""
    vis_map = [[0]*len(grid[0]) for row in grid]
    for _ in 'SENW':
        vis = get_visible_dir(grid)
        for i, row in enumerate(vis):
            for j, val in enumerate(row):
                vis_map[i][j] = vis_map[i][j] or val  # Visible from a direction.
        grid = rotate(grid)
        vis_map = rotate(vis_map)
    return vis_map

def count_visible(grid: list[list[int]]) -> int:
    """Add up all the ones."""
    vis_map = get_visible(grid)
    return sum(sum(row) for row in vis_map)

assert count_visible(INPUT) == 21


def get_each_visible(grid: list[list[int]]) -> list[list[int]]:
    """Count visible from a point."""
    vis = [[1]*len(grid[0]) for row in grid]
    for _ in 'SENW':
        for i, row in enumerate(vis):
            for j, val in enumerate(row):
                vis_row = get_visible_row(grid[i], [], j)
                vis[i][j] = val * sum(vis_row)  # Running product.
        grid = rotate(grid)
        vis = rotate(vis)
    return vis

def amax(grid: list[list[int]]) -> int:
    """Find the max value in a grid."""
    return max(max(row) for row in grid)

assert amax(get_each_visible(INPUT)) == 8, "Part 2 test failed."


if __name__ == "__main__":

    with open('data/day08.txt') as f:
        data = parse(f.read())

    part1 = count_visible(data)
    print('Part 1:', part1)
    assert part1 == 1814

    part2 = amax(get_each_visible(data))
    print('Part 2:', part2)
