import os
import re
from argparse import Namespace

from .models import File, Directory


def solve(args: Namespace):
    """
    Solve the disk space puzzle.
    """
    dirname = os.path.dirname(__file__)
    basefile = "sample.txt" if args.test else "input.txt"
    input_file = os.path.join(dirname, basefile)

    print("Disk space")
    print(f"loading {input_file}")

    # Create the root directory
    root = Directory(name="/")
    cwd = root

    with open(input_file, "r", encoding="utf8") as fh:
        for line in fh.readlines():
            if match := re.search(r"^\$ cd (?P<directory>.*)", line):
                # change the working directory
                name = match.group("directory")

                # handle the special cases
                if name == "/":
                    cwd = root
                    continue
                if name == "..":
                    assert cwd.parent, f"{cwd} has no parent"
                    cwd = cwd.parent if cwd.parent else root
                    continue

                # try to move into a sub directory
                if subdirs := [d for d in cwd.subdirectories if name == d.name]:
                    assert subdirs[0]
                    cwd = subdirs[0]

                continue

            if match := re.search(r"^\$ ls", line):
                # the ls command is a no-op for us
                continue

            if match := re.search(r"^dir (?P<directory>.*)", line):
                # add this subdirectory to working directory
                name = match.group("directory")
                cwd.subdirectories.append(Directory(name=name, parent=cwd))

            if match := re.search(r"^(?P<size>\d+) (?P<file>.*)", line):
                # add this file to working directory
                name = match.group("file")
                size = match.group("size")
                cwd.files.append(File(name=name, size=int(size)))
                pass

    print(f"Root size is {root.size}")
    root.pprint()

    # Puzzle 1
    # Find all of the directories with a total size of at most 100000.
    # What is the sum of the total sizes of those directories?
    max_size = 100000
    dirs = root.max_size_candidates(max_size)
    total_candidate_size = sum([size for _, size in dirs])
    print(f"Flattened dirs {[(d.name, size) for d, size in dirs]}")
    print(f"Total size candidates is {total_candidate_size}")

    # Puzzle 2
    # Find the smallest directory that, if deleted, would free up enough space on the
    # filesystem to run the update.
    # What is the total size of that directory?
    total_disk_space = 70000000
    need_space = 30000000
    unused_space = total_disk_space - root.size
    need_to_delete = need_space - unused_space
    print(f"Unused space is {unused_space} :: Need to delete {need_to_delete}")

    dirs = root.min_size_candidates(need_to_delete)
    sorted_dirs = sorted([i for i in dirs], key=lambda x: x[1], reverse=True)
    candidate, candidate_size = sorted_dirs.pop()
    print(f"Flattened dirs {[(d.name, size) for d, size in sorted_dirs]}")
    print(f"Delete {candidate.name} {candidate_size}")
