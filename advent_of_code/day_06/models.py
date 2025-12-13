"""
Models for Day 6: Trash Compactor.
"""


class Equations:
    workings: list[tuple[int, int]] | None = None
    answers: list[int] | None = None

    def __init__(self) -> None:
        self.workings = None

    def add_line(self, data: list[str]) -> None:
        if self.workings is None:
            self.workings = [(0, 1)] * len(data)
        if self.answers is None:
            self.answers = [0] * len(data)

        for index, value in enumerate(data):
            working = self.workings[index]
            if value.isnumeric():
                self.workings[index] = (
                    working[0] + int(value),
                    working[1] * int(value),
                )
            else:
                # Keep the tuple value for the operator, zero out the other value
                match value:
                    case "+":
                        self.answers[index] = working[0]
                    case "*":
                        self.answers[index] = working[1]

    def get_total(self) -> int:
        return sum(self.answers)
