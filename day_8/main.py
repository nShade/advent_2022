import itertools


def rotate_90(array):
    return list(zip(*reversed(list(array))))


def rotate_180(array):
    return rotate_90(rotate_90(array))


def rotate_270(array):
    return rotate_90(rotate_180(array))


def visible(row):
    highest = -1
    for tree in row:
        if tree > highest:
            yield 1
            highest = tree
        else:
            yield 0


def score(row):
    height_index = [0 for k in range(10)]
    for index, tree in enumerate(row):
        yield index - max(height_index[tree:])
        height_index[tree] = index


if __name__ == "__main__":
    with open("input", "r") as input_file:
        input_lines = input_file.readlines()

    tree_height_array = [[int(sym) for sym in line[:-1]] for line in input_lines]
    tree_height_array_90 = rotate_90(tree_height_array)
    tree_height_array_180 = rotate_90(tree_height_array_90)
    tree_height_array_270 = rotate_90(tree_height_array_180)

    visible_left = itertools.chain(*map(visible, tree_height_array))
    visible_bottom = itertools.chain(*rotate_270(map(visible, tree_height_array_90)))
    visible_right = itertools.chain(*rotate_180(map(visible, tree_height_array_180)))
    visible_top = itertools.chain(*rotate_90(map(visible, tree_height_array_270)))

    res_1 = sum(map(lambda a, b, c, d: 1 if a + b + c + d > 0 else 0,
                    visible_left, visible_bottom, visible_right, visible_top))
    print(f"Part 1: {res_1}")

    score_left = itertools.chain(*map(score, tree_height_array))
    score_bottom = itertools.chain(*rotate_270(map(score, tree_height_array_90)))
    score_right = itertools.chain(*rotate_180(map(score, tree_height_array_180)))
    score_top = itertools.chain(*rotate_90(map(score, tree_height_array_270)))
    res_2 = max(map(lambda a, b, c, d: a * b * c * d, score_left, score_right, score_top, score_bottom))
    print(f"Part 2: {res_2}")
