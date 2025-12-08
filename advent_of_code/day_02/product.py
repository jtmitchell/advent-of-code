"""
Dataclass for a Product.
"""

from dataclasses import dataclass


@dataclass
class Product_pt1:
    id: int

    def is_valid(self) -> bool:
        """
        Return true if the ID is valid.

        Invalid IDs are:
        * sequence of repeating digits.

        So we can ignore numbers whose string length is odd.

        """
        id_str: str = str(self.id)
        if len(id_str) % 2 == 1:
            return True

        # Divide the string into two parts
        mid_len: int = len(id_str) // 2
        start_part: str = id_str[:mid_len]
        end_part: str = id_str[mid_len:]

        return not bool(start_part == end_part)


@dataclass
class Product_pt2:
    id: int

    def is_valid(self) -> bool:
        """
        Return true if the ID is valid.

        Invalid IDs are:
        * sequence of repeating digits.

        Loop through the string, splitting into 2, then 3, then 4
        up to the length of the string, and check if each substring is equal.

        """
        id_str: str = str(self.id)
        for num_parts in range(1, len(id_str)):
            if self.is_repeating_string(parts=num_parts):
                self._num_parts = num_parts
                return False

        return True

    def is_repeating_string(self, parts: int) -> bool:
        """Return True if all the substrings are equal."""
        id_str: str = str(self.id)
        # Divide the string into parts
        self._substrings = [id_str[i : i + parts] for i in range(0, len(id_str), parts)]
        return len(set(self._substrings)) <= 1
