# Define rules for game
from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class Rule:
    beats: HandShape
    loses: HandShape


@dataclass
class HandShape:
    symbols: list[str]
    score: int
    rule: Optional[Rule] = None


ROCK = HandShape(score=1, symbols=["A", "X"])
PAPER = HandShape(score=2, symbols=["B", "Y"])
SCISSORS = HandShape(score=3, symbols=["C", "Z"])

ROCK.rule = Rule(beats=SCISSORS, loses=PAPER)
PAPER.rule = Rule(beats=ROCK, loses=SCISSORS)
SCISSORS.rule = Rule(beats=PAPER, loses=ROCK)


@dataclass
class GameRound:
    my_shape: HandShape
    opponent_shape: HandShape

    DRAW = 3
    WIN = 6

    @property
    def score(self) -> int:
        """
        Return the score for the round.
        """
        # Check for a draw
        if self.my_shape == self.opponent_shape:
            return self.my_shape.score + self.DRAW

        # Check for a win
        assert self.my_shape.rule is not None
        if self.my_shape.rule.beats == self.opponent_shape:
            return self.my_shape.score + self.WIN

        return self.my_shape.score

    @property
    def result(self) -> str:
        """
        Return the result of the round.
        """
        # Check for a draw
        if self.my_shape == self.opponent_shape:
            return "Draw"

        # Check for a win
        assert self.my_shape.rule is not None
        if self.my_shape.rule.beats == self.opponent_shape:
            return "Win"

        return "Lose"
