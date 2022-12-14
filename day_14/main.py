def process_input_lines(lines):
    rocks = set()
    for line in lines:
        rock_path = [[int(c) for c in coord.split(',')] for coord in line.split(' -> ')]
        for (x1, y1), (x2, y2) in zip(rock_path[:-1], rock_path[1:]):
            start_x, end_x = sorted([x1, x2])
            start_y, end_y = sorted([y1, y2])
            rocks |= {(x, y) for x in range(start_x, end_x + 1) for y in range(start_y, end_y + 1)}
    return rocks


def drop_sand_floor(rocks, start, floor):
    start_x, start_y = start

    if start_y + 1 == floor:
        return start
    if (start_x, start_y + 1) not in rocks:
        return drop_sand_floor(rocks, (start_x, start_y + 1), floor)
    if (start_x - 1, start_y + 1) not in rocks:
        return drop_sand_floor(rocks, (start_x - 1, start_y + 1), floor)
    if (start_x + 1, start_y + 1) not in rocks:
        return drop_sand_floor(rocks, (start_x + 1, start_y + 1), floor)

    return start


def comes_to_rest(rocks):
    bottom = max([y for x, y in rocks])
    units = 0
    sand = set()

    while True:
        final_unit_position = drop_sand_floor(rocks | sand, (500, 0), bottom + 2)
        if final_unit_position[1] == bottom + 1:
            break
        units += 1
        sand |= {final_unit_position}

    yield units
    sand = set([(500, 0)])
    sand_row = set([(500, 0)])
    for y in range(0, bottom + 1):
        sand_row = ({(x + 1, y + 1) for x, y in sand_row} | {(x - 1, y + 1) for x, y in sand_row} | {(x, y + 1) for x, y in sand_row}) - rocks
        sand |= sand_row

    yield len(sand)


if __name__ == "__main__":
    with open("input", "r") as input_file:
        input_lines = input_file.readlines()

    rocks = process_input_lines(input_lines)
    result = comes_to_rest(rocks)
    print(f"Part 1: {next(result)}")
    print(f"Part 2: {next(result)}")
