import functools
import json


def is_right_order(item_1, item_2):
    """
    >>> is_right_order(2, 3)
    True
    >>> is_right_order(3, 2)
    False
    >>> is_right_order(3, 3)
    >>> is_right_order([4], [7])
    True
    >>> is_right_order([7], [4])
    False
    >>> is_right_order([4], [4, 4])
    True
    >>> is_right_order([4, 4], [4])
    False
    >>> is_right_order([4, 4], [4, 4])
    """
    if isinstance(item_1, int) and isinstance(item_2, int):
        if item_1 == item_2:
            return None
        return item_1 < item_2

    if isinstance(item_1, int):
        return is_right_order([item_1], item_2)

    if isinstance(item_2, int):
        return is_right_order(item_1, [item_2])

    for index, element_2 in enumerate(item_2):
        try:
            result = is_right_order(item_1[index], element_2)
            if result is not None:
                return result
        except IndexError:
            return True

    if len(item_1) > len(item_2):
        return False


def compare_packets(p1, p2):
    if is_right_order(p1, p2):
        return -1

    return 1


if __name__ == "__main__":
    with open("input", "r") as input_file:
        input_text = input_file.read()

    pairs = list(
        map(lambda x: (json.loads(x[0]), json.loads(x[1])), map(lambda x: x.split('\n'), input_text.split('\n\n'))))

    res_1 = sum([i + 1 for i, pair in enumerate(pairs) if is_right_order(*pair)])
    print(f"Part 1: {res_1}")
    packets = [a for a, b in pairs] + [b for a, b in pairs] + [[[2]], [[6]]]
    sorted_packets = sorted(packets, key=functools.cmp_to_key(compare_packets))
    res_2 = (sorted_packets.index([[2]]) + 1) * (sorted_packets.index([[6]]) + 1)
    print(f"Part 2: {res_2}")
