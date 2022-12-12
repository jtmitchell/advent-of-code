from dataclasses import dataclass, field
from typing import Iterator, Optional
import math

# pylint: disable=too-many-instance-attributes


@dataclass
class Monkey:
    """
    Class for Monkey.
    """

    id: int
    test_divisible: int
    monkey_true: int
    monkey_false: int
    operation: tuple[str, str]
    items: list[int] = field(default_factory=list)
    total_inspections: int = 0
    relief: Optional[int] = None

    def inspect_items(self, least_common_multiple: float) -> Iterator[tuple[int, int]]:
        """
        Inspect the item.
        """
        for _ in range(len(self.items)):
            self.total_inspections += 1
            # Take the item out of monkey's list
            item = self.items.pop(0)
            worry = item

            # Calculate the worry level
            if self.operation[1].isnumeric():
                op_value = int(self.operation[1])
            else:
                op_value = worry

            assert self.operation[0] in ["*", "+"]
            if self.operation[0] == "*":
                worry = worry * op_value
            else:
                worry = worry + op_value

            if self.relief:
                worry = int(worry / self.relief)
            else:
                worry = int(worry % least_common_multiple)

            # Perform worry test
            if worry % self.test_divisible == 0:
                yield worry, self.monkey_true
            else:
                yield worry, self.monkey_false


@dataclass
class Troop:
    """
    Class for a troop of monkeys.
    """

    monkeys: list[Monkey] = field(default_factory=list)

    @property
    def least_common_multiple(self) -> float:
        """
        Return the least common multiple of all the divisors.
        """
        divisors = [m.test_divisible for m in self.monkeys]
        return math.prod(divisors)

    def monkey_business(self, least_common_multiple: float):
        """
        Perform a round of inspections.
        """
        for m in self.monkeys:
            for item, target in m.inspect_items(least_common_multiple):
                self.monkeys[target].items.append(item)

    def show_hands(self) -> None:
        """
        Pretty print the items.
        """
        for m in self.monkeys:
            print(f"Monkey {m.id}: {m.items} ({m.total_inspections})")
