import os
from argparse import Namespace


def scenic_score(target: int, trees: list[int]) -> int:
    """
    Return the scenic score looking down the path of trees.
    """
    score = 0
    for i in trees:
        score += 1
        if i >= target:
            break
    return score


def solve(args: Namespace):
    """
    Solve the tree house puzzle.
    """
    dirname = os.path.dirname(__file__)
    basefile = "sample.txt" if args.test else "input.txt"
    input_file = os.path.join(dirname, basefile)

    print("Tree house")
    print(f"loading {input_file}")

    forest = []
    with open(input_file, "r", encoding="utf8") as fh:
        for line in fh.readlines():
            # Each integer in the line is the height of a tree
            forest.append([int(i) for i in line.strip()])

    forest_columns = [list(x) for x in zip(*forest)]

    pp_forest = "\n".join([str(i) for i in forest])
    print(f"Forest rows \n{pp_forest}")
    pp_forest = "\n".join([str(i) for i in forest_columns])
    print(f"Forest columns \n{pp_forest}")

    visible_trees = []
    scenic_trees = []
    for row_idx, row in enumerate(forest):
        for col_idx, tree in enumerate(row):
            assert tree == forest_columns[col_idx][row_idx]
            column = forest_columns[col_idx]
            if col_idx in [0, len(row) - 1] or row_idx in [0, len(column) - 1]:
                # Trees on the boundary are always visible
                visible_trees.append((tree, row_idx, col_idx))
                continue
            else:
                # Tree is visible if the height is greater than any heights to the boundary
                # by row or by columns.
                visible_left = tree > max(row[:col_idx])
                visible_right = tree > max(row[col_idx + 1 :])
                visible_top = tree > max(column[:row_idx])
                visible_bottom = tree > max(column[row_idx + 1 :])

                if visible_left or visible_right or visible_top or visible_bottom:
                    visible_trees.append((tree, row_idx + 1, col_idx + 1))

                # Scenic score is found by multpling the number of trees to boundary,
                # until blocked
                scenic_left = scenic_score(tree, list(reversed(row[:col_idx])))
                scenic_right = scenic_score(tree, row[col_idx + 1 :])
                scenic_top = scenic_score(tree, list(reversed(column[:row_idx])))
                scenic_bottom = scenic_score(tree, column[row_idx + 1 :])
                scenic_trees.append(
                    scenic_left * scenic_right * scenic_top * scenic_bottom
                )

    # Puzzle 1
    # How many trees are visible from outside the grid?
    print(f"Number of visible trees is {len(visible_trees)}")
    if args.test:
        pp_forest = "\n".join([str(i) for i in visible_trees])
        # print(f"Visible trees rows \n{pp_forest}")

        assert (
            len(visible_trees) == 21
        ), f"Incorrect visible trees {len(visible_trees)} is not 21"

    # Puzzle 2
    # What is the highest scenic score possible for any tree?
    print(f"Highest of scenic score is {max(scenic_trees)}")
    if args.test:
        assert (
            max(scenic_trees) == 8
        ), f"Incorrect scenic score {max(scenic_trees)} is not 8"
