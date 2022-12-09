from typing import Literal


def move_head(pos: tuple[int, int], movement_direction: Literal["U", "D", "L", "R"]):
    x, y = pos
    if movement_direction == "U":
        return x, y + 1
    if movement_direction == "D":
        return x, y - 1
    if movement_direction == "L":
        return x - 1, y
    if movement_direction == "R":
        return x + 1, y


def move_tail(tail: tuple[int, int], head: tuple[int, int]):
    tx, ty = tail
    hx, hy = head
    if tx - hx > 1:
        tx -= 1
        if ty < hy:
            ty += 1
        if ty > hy:
            ty -= 1
    if hx - tx > 1:
        tx += 1
        if ty < hy:
            ty += 1
        if ty > hy:
            ty -= 1
    if ty - hy > 1:
        ty -= 1
        if tx < hx:
            tx += 1
        if tx > hx:
            tx -= 1
    if hy - ty > 1:
        ty += 1
        if tx < hx:
            tx += 1
        if tx > hx:
            tx -= 1
    return tx, ty


def move_rope(movements: list[tuple[str, int]], knots: int):
    tail_visited = set()
    rope = [(0, 0) for i in range(knots)]

    tail_visited.add(rope[-1])

    for direction, distance in movements:
        for i in range(distance):
            rope[0] = move_head(rope[0], direction)
            for knot in range(1, knots):
                rope[knot] = move_tail(rope[knot], rope[knot - 1])
            tail_visited.add(rope[-1])

    return len(tail_visited)


if __name__ == "__main__":
    with open("input", "r") as input_file:
        input_lines = input_file.readlines()

    movements = [(line[0], int(line[1:])) for line in input_lines]
    tail_visited_1 = move_rope(movements, 2)
    print(f"Part 1: {tail_visited_1}")
    tail_visited_2 = move_rope(movements, 10)
    print(f"Part 2: {tail_visited_2}")
