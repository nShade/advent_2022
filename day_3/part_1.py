import string

PRIORITY = dict(**{x: ord(x) - 96 for x in string.ascii_lowercase}, **{x: ord(x) - 38 for x in string.ascii_uppercase})


def similar_item(items):
    half = len(items) // 2
    return (set(items[:half]) & set(items[half:])).pop()


def convert_line(line):
    return [PRIORITY[sym] for sym in line]


if __name__ == "__main__":
    with open("input", "r") as text_input:
        input_lines = text_input.readlines()

    res = sum([similar_item(convert_line(line.replace('\n', ''))) for line in input_lines])
    print(res)
