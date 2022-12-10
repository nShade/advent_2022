import itertools
import string

PRIORITY = dict(**{x: ord(x) - 96 for x in string.ascii_lowercase}, **{x: ord(x) - 38 for x in string.ascii_uppercase})


def similar_item(*items):
    return list(itertools.accumulate(items, lambda x, y: x & y))[-1].pop()


if __name__ == "__main__":
    with open("input", "r") as text_input:
        input_lines = text_input.readlines()

    priorities = [({PRIORITY[sym] for sym in line[:(len(line) - 1) // 2]},
                   {PRIORITY[sym] for sym in line[(len(line) - 1) // 2:-1]})
                  for line in input_lines]
    print(priorities)
    res_1 = sum([similar_item(*items) for items in priorities])
    print(f"Part 1: {res_1}")
    priorities = [{PRIORITY[sym] for sym in line[:-1]} for line in input_lines]
    chunked_list = list(itertools.zip_longest(*[priorities[i::3] for i in range(3)]))
    res_2 = sum([similar_item(*item) for item in chunked_list])
    print(f"Part 2: {res_2}")
