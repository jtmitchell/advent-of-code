from dataclasses import dataclass
import string

# Start with a space so the letter match position has correct index
# a = 1, z = 26, A = 27, Z = 52
PRIORITIES = f" {string.ascii_lowercase}{string.ascii_uppercase}"


@dataclass
class Rucksack:
    """
    Model for the elves rucksacks.
    """

    items: str

    @property
    def middle(self) -> int:
        """
        Return the middle of the string.
        """
        return int(len(self.items) / 2)

    @property
    def compartment1(self) -> str:
        """
        Return the contents of first compartment.
        """
        return self.items[0 : self.middle]

    @property
    def compartment2(self) -> str:
        """
        Return the contents of second compartment.
        """
        return self.items[self.middle :]

    @property
    def shared_items(self) -> list[str]:
        """
        Return a list of items that exist in both compartments.
        """
        return [value for value in self.compartment1 if value in self.compartment2]

    @property
    def priority(self) -> int:
        """
        Return the priority of the unique shared items.
        """
        priorities = [PRIORITIES.find(i) for i in set(self.shared_items)]
        return sum(priorities)
