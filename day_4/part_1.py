import re


def contains(groups):
    return ((groups[0] <= groups[2]) and (groups[1] >= groups[3])) or \
           ((groups[0] >= groups[2]) and (groups[1] <= groups[3]))


if __name__ == "__main__":
    with open("input", "r") as text_input:
        input_lines = text_input.readlines()

    pattern = re.compile(r'(\d+)-(\d+),(\d+)-(\d+)')
    converted_lines = [[int(num) for num in pattern.match(line).groups()] for line in input_lines]
    res = sum([1 for line in converted_lines if contains(line)])
    print(res)
