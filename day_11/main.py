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


def monkey_test(operation, test, throw, manage, item):
    new = manage(eval(operation, {}, {'old': item}))
    return new, throw[new % test == 0]


def monkey_round(monkeys, manage):
    for i, (items, test) in enumerate(monkeys):
        yield len(items)

        for item in items:
            item, throw_to = test(manage, item)
            monkeys[throw_to][0] += [item]

        monkeys[i][0] = []


def calculate_monkey_business(monkeys, manage, rounds):
    res = [monkey_round(monkeys, manage) for i in range(rounds)]
    inspected = list(map(sum, zip(*list(map(list, res)))))
    two_most_active = sorted(inspected)[-2:]
    return two_most_active[0] * two_most_active[1]


if __name__ == "__main__":
    with open("input", "r") as input_file:
        input_text = input_file.read()

    parsed_text = [monkey_dict for monkey_dict in MONKEY_PATTERN.finditer(input_text)]
    monkeys = [[[int(item) for item in monkey_dict['items'].split(", ")],
                functools.partial(monkey_test,
                                  monkey_dict['operation'],
                                  int(monkey_dict['test']),
                                  {True: int(monkey_dict['test_positive_throw']),
                                   False: int(monkey_dict['test_negative_throw'])})]
               for monkey_dict in parsed_text]
    monkeys_2 = copy.deepcopy(monkeys)

    monkey_business = calculate_monkey_business(monkeys, lambda x: x // 3, 20)
    print(f"Part 1: {monkey_business}")

    tests = [int(monkey_dict['test']) for monkey_dict in parsed_text]
    *_, divisor = itertools.accumulate(tests, lambda a, b: a * b)
    monkey_business = calculate_monkey_business(monkeys_2, lambda x: x % divisor, 10000)
    print(f"Part 2: {monkey_business}")
