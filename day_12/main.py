import string


def elevation(sym):
    if sym == 'S':
        return 1
    if sym == 'E':
        return 26
    return ord(sym) - 96


def is_path_exists(sym_from, sym_to):
    if sym_to not in (string.ascii_lowercase + "SE"):
        return False
    return elevation(sym_to) - elevation(sym_from) < 2


def find_path(solutions, paths, start, end, moves=0):
    start_y, start_x = start

    if start == end:
        return 0

    if solutions[start_y][start_x] is not None and solutions[start_y][start_x] <= moves:
        return None

    solutions[start_y][start_x] = moves
    is_path_right, is_path_left, is_path_down, is_path_up = paths[start_y][start_x]

    path_r, path_l, path_d, path_u = None, None, None, None

    if is_path_right:
        path_r = find_path(solutions, paths, (start_y, start_x + 1), end, moves + 1)
    if is_path_left:
        path_l = find_path(solutions, paths, (start_y, start_x - 1), end, moves + 1)
    if is_path_down:
        path_d = find_path(solutions, paths, (start_y + 1, start_x), end, moves + 1)
    if is_path_up:
        path_u = find_path(solutions, paths, (start_y - 1, start_x), end, moves + 1)

    if path_u == path_d == path_r == path_l is None:
        return None

    res = min([i for i in (path_r, path_l, path_d, path_u) if i is not None]) + 1
    return res


if __name__ == "__main__":
    with open("input", "r") as input_file:
        input_lines = input_file.readlines()

    width = len(input_lines[0]) - 1
    height = len(input_lines)

    paths = ()
    start, end = None, None
    for i, (line, line_below, line_above) \
            in enumerate(zip(input_lines,
                             input_lines[1:] + ["~" * len(input_lines[0])],
                             ["~" * len(input_lines[0])] + input_lines[:-1])):
        p = ()
        for j, (symbol, symbol_right, symbol_left, symbol_below, symbol_above) \
                in enumerate(zip(line[:-1],
                                 line[1:],
                                 "~" + line[:-2],
                                 line_below[:-1],
                                 line_above[:-1])):
            if symbol == 'S':
                start = (i, j)
            if symbol == 'E':
                end = (i, j)
            p += ((is_path_exists(symbol, symbol_right),
                   is_path_exists(symbol, symbol_left),
                   is_path_exists(symbol, symbol_below),
                   is_path_exists(symbol, symbol_above)),)

        paths += (p,)

    solutions = [[None for i in range(width)] for j in range(height)]

    res_1 = find_path(solutions, paths, start, end)
    print(f"Part 1: {res_1}")
    res_2 = "IDK"
    print(f"Part 2: {res_2}")
