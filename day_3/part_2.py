import string
from itertools import zip_longest

PRIORITY = dict(**{x: ord(x) - 96 for x in string.ascii_lowercase}, **{x: ord(x) - 38 for x in string.ascii_uppercase})


def similar_item(a, b, c):
    return (set(a) & set(b) & set(c)).pop()


def convert_line(line):
    return [PRIORITY[sym] for sym in line]


if __name__ == "__main__":
    with open("input", "r") as text_input:
        input_lines = text_input.readlines()

    converted_list = [convert_line(line.replace('\n', '')) for line in input_lines]
    chunked_list = list(zip_longest(*[converted_list[i::3] for i in range(3)]))
    res = sum([similar_item(*item) for item in chunked_list])
    print(res)

