import itertools


def calculate_row_score(heights):
    height_index = [0 for k in range(10)]
    for index, height in enumerate(heights):
        yield index - max(height_index[height:])
        height_index[height] = index


if __name__ == "__main__":
    with open("input", "r") as input_file:
        input_lines = input_file.readlines()

    tree_height_array = [[int(sym) for sym in line[:-1]] for line in input_lines]

    left_scores = [i for row in tree_height_array for i in calculate_row_score(row)]
    right_scores = [i for row in tree_height_array for i in list(calculate_row_score(row[::-1]))[::-1]]
    top_scores = itertools.chain(*zip(*[calculate_row_score(row) for row in zip(*tree_height_array)]))
    bottom_scores = itertools.chain(*zip(*[list(calculate_row_score(row[::-1]))[::-1] for row in zip(*tree_height_array)]))
    res = max(map(lambda a, b, c, d: a * b * c * d, left_scores, right_scores, top_scores, bottom_scores))
    print(res)
