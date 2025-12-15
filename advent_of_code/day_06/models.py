"""
Models for Day 6: Trash Compactor.
"""

import math
from dataclasses import dataclass


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


@dataclass
class Homework:
    numbers: list[str] | None = None
    operation: str = ""

    def answer(self) -> int:
        if self.operation == "+":
            return sum([int(i) for i in self.numbers])
        else:
            return math.prod([int(i) for i in self.numbers])


class VerticalEquations(Equations):
    data: list[str] | None = None
    workings: list[str] | None = None

    def add_line(self, data: str) -> None:
        if self.data is None:
            self.data = []
        self.data.append(data)

    def pivot(self) -> None:
        self.line_length = max([len(line) for line in self.data])
        self.workings: list[Homework] = []

        homework = None
        for index in range(self.line_length):
            value = ""
            for line in self.data:
                value += line[index] if index < len(line) else ""

            if not value.strip():
                continue

            if value[-1] in "*+":
                if homework is not None:
                    self.workings.append(homework)
                homework = Homework(operation=value[-1], numbers=[value[:-1].strip()])
            else:
                homework.numbers.append(value.strip())

        if homework is not None:
            self.workings.append(homework)

    def get_total(self) -> int:
        if self.workings is None:
            self.pivot()

        totals = [i.answer() for i in self.workings]
        return sum(totals)
