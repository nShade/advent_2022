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


def construct_paths(links, end, start, visited=set()):
    next_locations = {l for location in start for l in links[location] if l not in visited}
    if end in next_locations:
        return 1
    return 1 + construct_paths(links, end, next_locations, visited | next_locations)


if __name__ == "__main__":
    with open("input", "r") as input_file:
        input_lines = input_file.readlines()

    paths = {}
    possible_hike_starts = ()
    start, end = None, None
    for i, (line, line_below, line_above) \
            in enumerate(zip(input_lines,
                             input_lines[1:] + ["~" * len(input_lines[0])],
                             ["~" * len(input_lines[0])] + input_lines[:-1])):
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
            if symbol == 'a':
                possible_hike_starts += ((i, j),)

            location_paths = ()
            if is_path_exists(symbol, symbol_right):
                location_paths += ((i, j + 1),)
            if is_path_exists(symbol, symbol_left):
                location_paths += ((i, j - 1),)
            if is_path_exists(symbol, symbol_below):
                location_paths += ((i + 1, j),)
            if is_path_exists(symbol, symbol_above):
                location_paths += ((i - 1, j),)
            paths[(i, j)] = location_paths

    res_1 = construct_paths(paths, end, {start}, {start})
    print(f"Part 1: {res_1}")
    res_2 = construct_paths(paths, end, set(possible_hike_starts), set(possible_hike_starts))
    print(f"Part 2: {res_2}")
