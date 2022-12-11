import math
import re

MONKEY_PATTERN = re.compile(r"""Monkey (?P<monkey>\d):
  Starting items: (?P<items>(?:\d+, )*\d+)
  Operation: new = (?P<operation>.*)
  Test: divisible by (?P<test>\d+)
    If true: throw to monkey (?P<test_positive_throw>\d)
    If false: throw to monkey (?P<test_negative_throw>\d)""")


def monkey_test(item, operation, test):
    new = math.floor(eval(operation, {}, {'old': item}) / 3)
    return new, new % test == 0


def monkey_turn(items, operation, test):
    for item in items:
        yield monkey_test(item, operation, test)


def monkey_round(monkeys):
    for monkey_id in range(len(monkeys)):
        monkey = monkeys[monkey_id]
        yield len(monkey['items'])

        for item, test_result in monkey_turn(monkey['items'], monkey['operation'], monkey['test']):
            monkeys[monkey['throw'][test_result]]['items'].append(item)

        monkey['items'] = []


if __name__ == "__main__":
    with open("input", "r") as input_file:
        input_text = input_file.read()

    monkeys = {int(monkey_dict['monkey']): {'items': [int(item) for item in monkey_dict['items'].split(", ")],
                                            'test': int(monkey_dict['test']),
                                            'operation': monkey_dict['operation'],
                                            'throw': {True: int(monkey_dict['test_positive_throw']),
                                                      False: int(monkey_dict['test_negative_throw'])}}
               for monkey_dict in MONKEY_PATTERN.finditer(input_text)}

    inspected = list(map(sum, zip(*[list(monkey_round(monkeys)) for i in range(20)])))
    two_most_active = sorted(inspected)[-2:]
    monkey_business = two_most_active[0] * two_most_active[1]

    print(f"Part 1: {monkey_business}")
    res_2 = "IDK"
    print(f"Part 2: {res_2}")
