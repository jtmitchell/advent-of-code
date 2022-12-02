#!/usr/bin/env python3
import os
import argparse
from rules import GameRound, ROCK, PAPER, SCISSORS

parser = argparse.ArgumentParser()
parser.add_argument(
    "-t",
    "--test",
    help="Run against the test data",
    action="store_true",
)
parser.add_argument(
    "-2",
    "--newrules",
    help="Run using V2 of the rules",
    action="store_true",
)
args = parser.parse_args()

dirname = os.path.dirname(__file__)
basefile = "sample.txt" if args.test else "input.txt"
input_file = os.path.join(dirname, basefile)

print("Rock, Paper, Scossors")
print(f"loading {input_file}")

rounds = []
with open(input_file, "r", encoding="utf8") as fh:
    for line in fh.readlines():
        line = line.strip()
        if line:
            o = line.split(" ", maxsplit=2)
            for shape in [ROCK, PAPER, SCISSORS]:
                if o[0].upper() in shape.symbols:
                    opponent_shape = shape
                if not args.newrules:
                    # Using original rules
                    # interpret the 2nd character as the shape to play
                    if o[1].upper() in shape.symbols:
                        my_shape = shape

            if args.newrules:
                # Using new rules
                # interpret 2nd character as the desired outcome
                assert opponent_shape.rule is not None
                if o[1].upper() == "X":
                    # Lose
                    my_shape = opponent_shape.rule.beats
                elif o[1].upper() == "Y":
                    # Draw
                    my_shape = opponent_shape
                else:
                    # Win
                    my_shape = opponent_shape.rule.loses

            rounds.append(GameRound(my_shape=my_shape, opponent_shape=opponent_shape))

scores = [r.score for r in rounds]
results = [r.result for r in rounds]
total_score = sum(scores)

print(f"Results {results}")
print(f"Scores {scores}")
print(f"Played {len(rounds)} games")
print(f"Total score is {total_score}")
