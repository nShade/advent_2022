import re


def overlap(groups):
    return ((groups[0] <= groups[2]) and (groups[2] <= groups[1])) or \
           ((groups[0] <= groups[3]) and (groups[3] <= groups[1])) or \
           ((groups[2] <= groups[0]) and (groups[0] <= groups[3])) or \
           ((groups[2] <= groups[1]) and (groups[1] <= groups[3]))


if __name__ == "__main__":
    with open("input", "r") as text_input:
        input_lines = text_input.readlines()

    pattern = re.compile(r'(\d+)-(\d+),(\d+)-(\d+)')
    converted_lines = [[int(num) for num in pattern.match(line).groups()] for line in input_lines]
    res = sum([1 for line in converted_lines if overlap(line)])
    print(res)
