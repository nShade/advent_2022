import itertools


def rotate_90(array):
    return list(zip(*reversed(list(array))))


def rotate_180(array):
    return rotate_90(rotate_90(array))


def rotate_270(array):
    return rotate_90(rotate_180(array))


def calculate_visible(row):
    highest = -1
    for tree in row:
        if tree > highest:
            yield 1
            highest = tree
        else:
            yield 0


def calculate_score(row):
    height_index = [0 for k in range(10)]
    for index, tree in enumerate(row):
        yield index - max(height_index[tree:])
        height_index[tree] = index


def calculate_all_sides(array, func, combine):
    array_90 = rotate_90(array)
    array_180 = rotate_90(array_90)
    array_270 = rotate_90(array_180)
    left = itertools.chain(*map(func, array))
    bottom = itertools.chain(*rotate_270(map(func, array_90)))
    right = itertools.chain(*rotate_180(map(func, array_180)))
    top = itertools.chain(*rotate_90(map(func, array_270)))
    return map(combine, left, bottom, right, top)


if __name__ == "__main__":
    with open("input", "r") as input_file:
        input_lines = input_file.readlines()

    tree_height_array = [[int(sym) for sym in line[:-1]] for line in input_lines]

    visible = calculate_all_sides(tree_height_array, calculate_visible, lambda a, b, c, d: 1 if a + b + c + d > 0 else 0)
    res_1 = sum(visible)
    print(f"Part 1: {res_1}")

    score = calculate_all_sides(tree_height_array, calculate_score, lambda a, b, c, d: a * b * c * d)
    res_2 = max(score)
    print(f"Part 2: {res_2}")
