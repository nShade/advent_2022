from typing import Literal

SHIFT_HEAD = {"U": (0, 1),
              "D": (0, -1),
              "L": (-1, 0),
              "R": (1, 0)}

SHIFT_TAIL = {k: v for d in [{(dx, dy): (shift_x, shift_y),
                              (dy, dx): (shift_y, shift_x),
                              (-dx, -dy): (-shift_x, -shift_y),
                              (-dy, -dx): (-shift_y, -shift_x),
                              (-dx, dy): (-shift_x, shift_y),
                              (-dy, dx): (-shift_y, shift_x),
                              (dx, -dy): (shift_x, -shift_y),
                              (dy, -dx): (shift_y, -shift_x)}
                             for (dx, dy), (shift_x, shift_y)
                             in {(0, 2): (0, 1),
                                 (1, 2): (1, 1),
                                 (2, 2): (1, 1)}.items()] for k, v in d.items()}


def move_head(x: int, y: int, direction: Literal["U", "D", "L", "R"]):
    dx, dy = SHIFT_HEAD[direction]
    return x + dx, y + dy


def move_tail(tx: int, ty: int, hx: int, hy: int):
    dx, dy = SHIFT_TAIL.get((hx - tx, hy - ty), (0, 0))
    return tx + dx, ty + dy


def head_movements(movements):
    x, y = 0, 0
    for direction, distance in movements:
        for i in range(distance):
            x, y = move_head(x, y, direction)
            yield x, y


def tail_movements(head_positions):
    x, y = 0, 0
    for hx, hy in head_positions:
        x, y = move_tail(x, y, hx, hy)
        yield x, y


def move_rope(movements: list[tuple[str, int]], knots: int):
    head_positions = head_movements(movements)

    for i in range(knots - 1):
        tail_positions = tail_movements(head_positions)

    return len(set(tail_positions))


if __name__ == "__main__":
    with open("input", "r") as input_file:
        input_lines = input_file.readlines()

    movements = [(line[0], int(line[1:])) for line in input_lines]
    tail_visited_1 = move_rope(movements, 2)
    print(f"Part 1: {tail_visited_1}")
    tail_visited_2 = move_rope(movements, 10)
    print(f"Part 2: {tail_visited_2}")
