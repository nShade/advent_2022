import re

PATTERN_INPUT = re.compile(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)")


class Range:
    """
    >>> Range(0, 1)
    Range(0, 1)
    >>> Range(0, 1) - Range(0, 1)
    []
    >>> Range(0, 2) - Range(0, 1)
    [Range(2, 2)]
    >>> Range(1, 2) - Range(0, 1)
    [Range(2, 2)]
    >>> Range(0, 8) - Range(3, 5)
    [Range(0, 2), Range(6, 8)]
    """

    def __init__(self, l, r):
        self._l = l
        self._r = r

    def __sub__(self, other):
        if other._r < self._l:
            return [Range(self._l, self._r)]
        if other._l > self._r:
            return [Range(self._l, self._r)]
        if other._l <= self._l and other._r >= self._r:
            return []
        if other._l <= self._l:
            return [Range(other._r + 1, self._r)]
        if other._r >= self._r:
            return [Range(self._l, other._l - 1)]

        return [Range(self._l, other._l - 1), Range(other._r + 1, self._r)]

    def __str__(self):
        return f'Range({self._l}, {self._r})'

    def __repr__(self):
        return str(self)


def visible_range(sensor_x, sensor_y, vision_distance, min_x, max_x, min_y, max_y):
    """
    >>> list(visible_range(2, 2, 4, 0, 0, -3, -3))
    [None]
    >>> list(visible_range(2, 2, 4, 0, 0, -2, -2))
    [[2, 2]]
    >>> list(visible_range(2, 2, 4, 0, 0, -1, -1))
    [[1, 3]]
    >>> list(visible_range(2, 2, 4, 0, 0, 0, 0))
    [[0, 4]]
    >>> list(visible_range(2, 2, 4, 0, 0, 1, 1))
    [[-1, 5]]
    >>> list(visible_range(2, 2, 4, 0, 0, 2, 2))
    [[-2, 6]]
    >>> list(visible_range(2, 2, 4, 0, 0, 3, 3))
    [[-1, 5]]
    >>> list(visible_range(2, 2, 4, 0, 0, 4, 4))
    [[0, 4]]
    >>> list(visible_range(2, 2, 4, 0, 0, 6, 6))
    [[2, 2]]
    >>> list(visible_range(2, 2, 4, 0, 0, 7, 7))
    [None]
    >>> list(visible_range(2, 2, 4, 0, 0, 0, 8))
    [[0, 4], [-1, 5], [-2, 6], [-1, 5], [0, 4], [1, 3], [2, 2], None, None]
    >>> list(visible_range(2, 2, 4, 0, 0, -8, 8))
    [None, None, None, None, None, None, [2, 2], [1, 3], [0, 4], [-1, 5], [-2, 6], [-1, 5], [0, 4], [1, 3], [2, 2], None, None]
    """
    y = min_y
    while y < min(sensor_y - vision_distance, max_y + 1):
        yield None
        y += 1

    vision_distance_x = vision_distance - (sensor_y - y)
    while y < min(sensor_y, max_y + 1):
        yield [sensor_x - vision_distance_x, sensor_x + vision_distance_x]
        vision_distance_x += 1
        y += 1

    vision_distance_x = vision_distance - (y - sensor_y)
    while y <= min(sensor_y + vision_distance, max_y):
        yield [sensor_x - vision_distance_x, sensor_x + vision_distance_x]
        vision_distance_x -= 1
        y += 1

    while y <= max_y:
        yield None
        y += 1


if __name__ == "__main__":
    with open("input", "r") as input_file:
        input_lines = input_file.readlines()

    positions = [list(map(int, PATTERN_INPUT.match(line).groups())) for line in input_lines]
    vision = [((sensor_x, sensor_y), abs(beacon_x - sensor_x) + abs(beacon_y - sensor_y))
              for sensor_x, sensor_y, beacon_x, beacon_y in positions]

    ranges = filter(None, [next(visible_range(sensor_x, sensor_y, distance, 0, 0, 2000000, 2000000)) for
                           (sensor_x, sensor_y), distance in vision])

    res = set()
    for a, b in ranges:
        res |= set(range(a, b))

    res_1 = len(res)
    print(f"Part 1: {res_1}")
    ranges = [visible_range(sensor_x, sensor_y, distance, 0, 0, 0, 4000000)
              for (sensor_x, sensor_y), distance in vision]

    for y in range(4000000):
        not_visible = [Range(0, 4000000)]
        for a, b in filter(None, [next(r) for r in ranges]):
            not_visible = [t for not_visible_range in not_visible for t in (not_visible_range - Range(a, b))]

        if not_visible:
            res_2 = not_visible[0]._l * 4000000 + y
            print(f"Part 2: {res_2}")
