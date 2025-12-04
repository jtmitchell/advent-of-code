"""
Dataclass for a Product.
"""

from dataclasses import dataclass


@dataclass
class Product:
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
