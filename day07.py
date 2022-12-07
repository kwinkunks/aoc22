"""
Advent of Code 2022
Day 6
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

def parse(data: str) -> dict:
    """Parse the directory listings, accumulating the sizes of directories.
    Directories are marked in the data by a line starting with 'dir' followed
    by the name of the directory. Files are denoted by a line containing the
    file size followed by the file name.

    Returns a dictionary of the total accumulated size of each directory,
    including all its subdirectories.
    """
    path = []
    sizes = {}
    for line in data:
        if line.startswith('$ cd'):
            if line == '$ cd ..':
                path.pop()
            else:
                path.append(line[5:])
        elif line.startswith('$ ls'):
            continue
        elif line.startswith('dir'):
            continue
        else:
            size, _ = line.split()
            sizes[tuple(path)] = sizes.get(tuple(path), 0) + int(size)
    return sizes

def get_dir_sizes(sizes):
    """Given a dictionary of directory sizes, return a dictionary of the
    sizes of each directory, including its subdirectories.
    """
    dirs = {}
    for path, size in sizes.items():
        for dir in path:
            dirs[dir] = dirs.get(dir, 0) + size
    return dirs

def sum_small_dirs(dirs, limit=100_000):
    """Given a dictionary of directory sizes, return the total size of those directories
    whose size is less than or equal to the given limit.
    """
    return sum(size for dir, size in dirs.items() if size <= limit)

assert sum_small_dirs(get_dir_sizes(parse(INPUT))) == 95437

if __name__ == "__main__":

    with open('data/day07.txt') as f:
        data = f.read().splitlines()

    print(sum_small_dirs(get_dir_sizes(parse(data))))
