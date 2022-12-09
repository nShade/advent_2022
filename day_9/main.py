def move_head(x, y, movement_direction):
    if movement_direction == "U":
        return x, y + 1
    if movement_direction == "D":
        return x, y - 1
    if movement_direction == "L":
        return x - 1, y
    if movement_direction == "R":
        return x + 1, y


def move_tail(tx, ty, hx, hy):
    if tx - hx > 1:
        tx -= 1
        if ty != hy:
            ty = hy
    if hx - tx > 1:
        tx += 1
        if ty != hy:
            ty = hy
    if ty - hy > 1:
        ty -= 1
        if tx != hx:
            tx = hx
    if hy - ty > 1:
        ty += 1
        if tx != hx:
            tx = hx
    return tx, ty


def move_rope(movements, knots):
    tail_visited = set()
    rope = [(0, 0) for i in range(knots)]
    tail_visited.add((0, 0))
    for direction, distance in movements:
        for i in range(distance):
            rope[0] = move_head(rope[0][0], rope[0][1], direction)
            for knot in range(1, knots):
                rope[knot] = move_tail(rope[knot][0], rope[knot][1], rope[knot - 1][0], rope[knot - 1][1])
            tail_visited.add((rope[-1][0], rope[-1][1]))

    return len(tail_visited)


if __name__ == "__main__":
    with open("input", "r") as input_file:
        input_lines = input_file.readlines()

    movements = [(line[0], int(line[1:])) for line in input_lines]
    tail_visited_1 = move_rope(movements, 2)
    print(f"Part 1: {tail_visited_1}")
    tail_visited_2 = move_rope(movements, 10)
    print(f"Part 2: {tail_visited_2}")