def find_marker(input, marker_length=4):
    """
    >>> find_marker("abcd", 4)
    4
    >>> find_marker("abcbde", 4)
    6
    """
    last_index = {}
    non_unique = 0
    for index, sym in enumerate(input):
        sym_last_index = last_index.get(sym, -1)
        last_index[sym] = index
        if index - sym_last_index > marker_length:
            non_unique -= 1
            if non_unique == 0:
                return index + 1
        else:
            non_unique = max(non_unique - 1, marker_length - (index - sym_last_index))


if __name__ == "__main__":
    with open("input", "r") as input_file:
        text = input_file.read()

    print(f"Part 1: {find_marker(text)}")
    print(f"Part 2: {find_marker(text, 14)}")
