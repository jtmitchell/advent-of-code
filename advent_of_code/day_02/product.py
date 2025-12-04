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

        """
        if self.id % 2 == 1:
            return True

        return False
