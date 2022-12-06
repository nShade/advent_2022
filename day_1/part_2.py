def convert_lines(lines):
    """
    >>> convert_lines(["1\\n", "2\\n", "\\n", "3\\n"])
    [[1, 2], [3]]
    """
    try:
        delimiter_index = lines.index('\n')
    except ValueError:
        return [[int(line) for line in lines]]

    return [[int(line) for line in lines[:delimiter_index]]] + convert_lines(lines[delimiter_index + 1:])


def max_calories(calories):
    """
    >>> max_calories([[0, 2, 4], [2, 1, 9], [1, 1], [4]])
    22
    """
    return sum(sorted([sum(elf) for elf in calories])[-3:])


if __name__ == "__main__":
    with open("input", "r") as text_input:
        input_lines = text_input.readlines()
        result = max_calories(convert_lines(input_lines))
        print(result)
