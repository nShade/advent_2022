import json


def compare(item_1, item_2):
    """
    >>> compare(2, 3)
    True
    >>> compare(3, 2)
    False
    >>> compare(3, 3)
    >>> compare([4], [7])
    True
    >>> compare([7], [4])
    False
    >>> compare([4], [4, 4])
    True
    >>> compare([4, 4], [4])
    False
    >>> compare([4, 4], [4, 4])
    """
    if isinstance(item_1, int) and isinstance(item_2, int):
        if item_1 == item_2:
            return None
        return item_1 < item_2

    if isinstance(item_1, int):
        return compare([item_1], item_2)

    if isinstance(item_2, int):
        return compare(item_1, [item_2])

    for index, element_2 in enumerate(item_2):
        try:
            result = compare(item_1[index], element_2)
            if result is not None:
                return result
        except IndexError:
            return True

    if len(item_1) > len(item_2):
        return False


if __name__ == "__main__":
    with open("input", "r") as input_file:
        input_text = input_file.read()

    pairs = list(
        map(lambda x: (json.loads(x[0]), json.loads(x[1])), map(lambda x: x.split('\n'), input_text.split('\n\n'))))

    res_1 = sum([i + 1 for i, pair in enumerate(pairs) if compare(*pair)])
    print(f"Part 1: {res_1}")
    res_2 = "IDK"
    print(f"Part 2: {res_2}")
