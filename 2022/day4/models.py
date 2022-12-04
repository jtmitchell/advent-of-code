from dataclasses import dataclass


@dataclass
class Assignment:
    """
    Class for elf cleanup assignment.
    """

    assignment: str

    @property
    def range(self) -> set[int]:
        """
        Expand the assignment to the full range.
        """
        (start, end) = self.assignment.split("-")
        return set(range(int(start), int(end) + 1))


@dataclass
class ElfPair:
    """
    Pair of elf cleanup assignments.
    """

    elf1: Assignment
    elf2: Assignment

    @property
    def is_full_overlap(self) -> bool:
        """
        Return True if the assignments fully overlap.
        """
        if self.elf1.range.issubset(self.elf2.range):
            return True
        if self.elf2.range.issubset(self.elf1.range):
            return True
        return False

    @property
    def is_partial_overlap(self) -> bool:
        """
        Return True if the assignments partially overlap.
        """
        overlap = [i for i in self.elf1.range if i in self.elf2.range]
        return bool(overlap)
