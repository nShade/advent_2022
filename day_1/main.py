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


if __name__ == "__main__":
    with open("input", "r") as text_input:
        input_lines = text_input.readlines()
        elves = convert_lines(input_lines)
        calories_per_elf = [sum(elf) for elf in elves]
        result_1 = max(calories_per_elf)
        print(f"Part 1: {result_1}")
        result_2 = sum(sorted(calories_per_elf)[-3:])
        print(f"Part 2: {result_2}")
