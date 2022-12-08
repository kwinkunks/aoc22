"""
Advent of Code 2022
Day 7
"""
RAW = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

INPUT = RAW.splitlines()


def parse(data: list[str]) -> dict:
    """
    Parse the directory listings, accumulating the sizes of directories.
    Directories are marked in the data by a line starting with 'dir' followed
    by the name of the directory. Files are denoted by a line containing the
    file size followed by the file name.

    Returns a dictionary of the total accumulated size of each directory,
    including all its subdirectories.
    """
    path: list[str] = []
    sizes: dict = {}
    for line in data:
        if line == '$ cd ..':
            path.pop()
        elif line.startswith('$ cd'):
            path.append(line[5:])
        elif line.startswith('$ ls'):
            continue
        elif line.startswith('dir'):
            continue
        else:
            size, _ = line.split()
            sizes[tuple(path)] = sizes.get(tuple(path), 0) + int(size)
    return sizes

def get_dir_sizes(sizes: dict[tuple[str], int]) -> dict:
    """
    Given a dictionary of directory sizes, return a dictionary of the
    sizes of each directory, including its subdirectories.
    """
    dirs: dict = {}
    for path, size in sizes.items():
        p = list(path)
        while p:
            dirs[tuple(p)] = dirs.get(tuple(p), 0) + size
            p.pop()
    return dirs

def sum_small_dirs(dirs: dict[tuple[str, ...], int], limit: int=100_000) -> int:
    """
    Given a dictionary of directory sizes, return the total size of those
    directories whose size is less than or equal to the given limit.
    """
    return sum(size for _, size in dirs.items() if size <= limit)

assert sum_small_dirs(get_dir_sizes(parse(INPUT))) == 95437


def find_smallest(dirs: dict[tuple[str, ...], int], total: int, required: int) -> int:
    """
    Given a dictionary of directory sizes, return the size of the smallest
    directory that is larger than the given required size.
    """
    freespace = total - dirs[('/',)]
    want = required - freespace
    smallest = total
    for _, size in get_dir_sizes(parse(data)).items():
        if (size > want) and (size < smallest):
            smallest = size
    assert smallest > want
    return smallest


if __name__ == "__main__":

    with open('data/day07.txt') as f:
        data = f.read().splitlines()

    part1 = sum_small_dirs(get_dir_sizes(parse(data)))
    print('Part 1:', part1)
    assert part1 == 1447046

    part2 = find_smallest(get_dir_sizes(parse(data)), 70000000, 30000000)
    print('Part 2:', part2)
