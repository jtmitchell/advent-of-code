from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class File:
    """
    Class for a file in a directory.
    """

    name: str
    size: int


@dataclass
class Directory:
    """
    Class to represent directories and files.
    """

    name: str
    parent: Optional[Directory] = None
    subdirectories: list[Directory] = field(default_factory=list)
    files: list[File] = field(default_factory=list)

    @property
    def size(self) -> int:
        """
        Return the total size of all contained files.
        """
        return sum([d.size for d in self.subdirectories]) + sum(
            f.size for f in self.files
        )

    def pprint(self, indent: str = "") -> None:
        """
        Recursive print size of subdirs.
        """
        print(f"{indent}{self.name} {self.size}")
        for s in self.subdirectories:
            s.pprint(indent=f"{indent}  ")

    def max_size_candidates(self, size: int) -> list[tuple[Directory, int]]:
        """
        Return list of candidate directories and sizes.
        """
        dirs = [(d, d.size) for d in self.subdirectories if d.size <= size]
        for d in self.subdirectories:
            dirs.extend(d.max_size_candidates(size))
        return dirs

    def min_size_candidates(self, size: int) -> list[tuple[Directory, int]]:
        """
        Return list of candidate directories and sizes.
        """
        dirs = [(d, d.size) for d in self.subdirectories if d.size >= size]
        for d in self.subdirectories:
            dirs.extend(d.min_size_candidates(size))
        return dirs
