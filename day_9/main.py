from typing import Literal

SHIFT_HEAD = {"U": (0, 1),
              "D": (0, -1),
              "L": (-1, 0),
              "R": (1, 0)}


def shift_tail():
    tail_shifts = [(0, 2, 0, 1),
                   (1, 2, 1, 1),
                   (2, 2, 1, 1)]
    for j in range(4):
        for i, (dx, dy, shift_x, shift_y) in enumerate(tail_shifts):
            yield (dx, dy), (shift_x, shift_y)
            tail_shifts[i] = (dy, dx, shift_y, shift_x)
        for i, (dx, dy, shift_x, shift_y) in enumerate(tail_shifts):
            yield (dx, dy), (shift_x, shift_y)
            tail_shifts[i] = (dx, -dy, shift_x, -shift_y)


SHIFT_TAIL = {k: v for k, v in shift_tail()}


def move_head(x: int, y: int, direction: Literal["U", "D", "L", "R"]):
    dx, dy = SHIFT_HEAD[direction]
    return x + dx, y + dy


def move_tail(tx: int, ty: int, hx: int, hy: int):
    dx, dy = SHIFT_TAIL.get((hx - tx, hy - ty), (0, 0))
    return tx + dx, ty + dy


def head_movements(movements):
    pos = 0, 0
    for direction, distance in movements:
        for i in range(distance):
            pos = move_head(*pos, direction)
            yield pos


def tail_movements(head_positions):
    pos = 0, 0
    for hpos in head_positions:
        pos = move_tail(*pos, *hpos)
        yield pos


def move_rope(movements: list[tuple[str, int]], knots: int):
    positions = head_movements(movements)

    for i in range(knots - 1):
        positions = tail_movements(positions)

    return len(set(positions))


if __name__ == "__main__":
    with open("input", "r") as input_file:
        input_lines = input_file.readlines()

    movements = [(line[0], int(line[1:])) for line in input_lines]
    tail_visited_1 = move_rope(movements, 2)
    print(f"Part 1: {tail_visited_1}")
    tail_visited_2 = move_rope(movements, 10)
    print(f"Part 2: {tail_visited_2}")
