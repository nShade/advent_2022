def find_marker(input, length=4):
    """
    >>> find_marker("abcd", 4)
    4
    >>> find_marker("abcbde", 4)
    6
    """
    last = input[:length - 1]

    for i, letter in enumerate(input[length - 1:]):

        if len(set(last + letter)) == length:
            return i + length

        last = last[-(length - 2):] + letter

    return -1


if __name__ == "__main__":
    with open("input", "r") as input_file:
        text = input_file.read()

    print(f"Part 1: {find_marker(text)}")
    print(f"Part 1: {find_marker(text, 14)}")
