
with open("08/trees.txt") as file:
    data = file.read().splitlines()

complete_trees = []
for row in data:
    complete_trees.append([int(tree) for tree in row])

def print_trees(trees):
    for row in trees:
        print(''.join([str(tree) for tree in row]))

print_trees(complete_trees[:20])


def is_highest(covering: list[int], this_height: int) -> bool:
    """tree closest is first in list"""
    return not any(tree >= this_height for tree in covering)

# Some tests
assert is_highest([1,2,3], 4)
assert is_highest([], 4)
assert not is_highest([1,2,4], 4)
assert not is_highest([6,2,2], 4)



def is_visible(row_num: int, col_num: int, trees: list[list[int]]) -> bool:
    trees_left = trees[row_num][:col_num]
    trees_right = trees[row_num][col_num+1:]
    trees_top = [row[col_num] for row in trees[:row_num]]
    trees_bottom = [row[col_num] for row in trees[row_num+1:]]

    all_trees = [trees_left, trees_right, trees_top, trees_bottom]
    this_tree_height = trees[row_num][col_num]
    return any(is_highest(trees, this_tree_height) for trees in all_trees)

test_trees = [
    [1,2,3,4,5],
    [6,7,8,9,0],
    [1,4,3,4,5],
    [6,7,8,9,0],
]

# print_trees(test_trees)
assert is_visible(row_num=1, col_num=1, trees=test_trees)
assert is_visible(row_num=0, col_num=0, trees=test_trees)
assert is_visible(row_num=1, col_num=4, trees=test_trees)
assert not is_visible(row_num=2, col_num=2, trees=test_trees)


def tree_scores(trees) -> list[int]:
    visible_trees = []
    for row_num, row in enumerate(trees):
        for col_num, col in enumerate(row):
            if is_visible(row_num, col_num, trees):
                visible_trees.append(trees[row_num][col_num])
    return visible_trees


print("Number of visible trees (TEST): ", len(tree_scores(test_trees)))
print("Number of visible trees: ", len(tree_scores(complete_trees)))


# PART TWO ======


def number_of_trees_visible(trees: list[int], this_tree_height: int) -> int:
    count = 0
    for tree in trees:
        count += 1
        if tree >= this_tree_height:
            return count
    return count

assert number_of_trees_visible([1,2,3], 2) == 2
assert number_of_trees_visible([1,2,3], 3) == 3
assert number_of_trees_visible([1,3,3], 3) == 2
assert number_of_trees_visible([1,2,3], 4) == 3
assert number_of_trees_visible([], 4) == 0

def scenic_score(row_num: int, col_num: int, trees: list[list[int]]):
    this_tree_height = trees[row_num][col_num]
    score_left = number_of_trees_visible(trees[row_num][:col_num][::-1], this_tree_height)
    score_right = number_of_trees_visible(trees[row_num][col_num+1:], this_tree_height)
    score_top = number_of_trees_visible([row[col_num] for row in trees[:row_num]][::-1], this_tree_height)
    score_bottom = number_of_trees_visible([row[col_num] for row in trees[row_num+1:]], this_tree_height)

    return score_left * score_right * score_bottom * score_top

def get_tree_scores(trees) -> list[int]:
    tree_scores = []
    for row_num, row in enumerate(trees):
        for col_num, col in enumerate(row):
            score = scenic_score(row_num, col_num, trees)
            tree_scores.append(score)
    return tree_scores

print("Max scenic score: ", max(get_tree_scores(complete_trees)))
