import copy
import functools
import itertools
import re

MONKEY_PATTERN = re.compile(r"""Monkey (?P<monkey>\d):
  Starting items: (?P<items>(?:\d+, )*\d+)
  Operation: new = (?P<operation>.*)
  Test: divisible by (?P<test>\d+)
    If true: throw to monkey (?P<test_positive_throw>\d)
    If false: throw to monkey (?P<test_negative_throw>\d)""")


def monkey_test(operation, test, positive_throw, negative_throw, manage, item):
    new = manage(operation(item))
    return new, positive_throw if new % test == 0 else negative_throw


def calculate_monkey_business(monkeys, manage, rounds):
    inspected = [0 for i in range(len(monkeys))]
    for round in range(rounds):
        for i, (items, test) in enumerate(monkeys):
            for item in items:
                item, throw_to = test(manage, item)
                monkeys[throw_to][0].append(item)
                inspected[i] += 1

            monkeys[i][0] = []

    two_most_active = sorted(inspected)[-2:]
    return two_most_active[0] * two_most_active[1]


if __name__ == "__main__":
    with open("input", "r") as input_file:
        input_text = input_file.read()

    parsed_text = [monkey_dict for monkey_dict in MONKEY_PATTERN.finditer(input_text)]
    monkeys = [[[int(item) for item in monkey_dict['items'].split(", ")],
                functools.partial(monkey_test,
                                  eval("lambda old: " + monkey_dict['operation']),
                                  int(monkey_dict['test']),
                                  int(monkey_dict['test_positive_throw']),
                                  int(monkey_dict['test_negative_throw']))]
               for monkey_dict in parsed_text]
    monkeys_2 = copy.deepcopy(monkeys)

    monkey_business = calculate_monkey_business(monkeys, lambda x: x // 3, 20)
    print(f"Part 1: {monkey_business}")

    tests = [int(monkey_dict['test']) for monkey_dict in parsed_text]
    *_, divisor = itertools.accumulate(tests, lambda a, b: a * b)
    monkey_business = calculate_monkey_business(monkeys_2, lambda x: x % divisor, 10000)
    print(f"Part 2: {monkey_business}")
