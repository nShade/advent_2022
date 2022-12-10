import copy
import itertools
import re

PROCEDURE_PATTERN = re.compile(r'move (\d+) from (\d+) to (\d+)')


def process_crates(crates):
    crates.reverse()
    index_positions = {index: pos for pos, index in enumerate(crates[0]) if index not in [' ', '\n']}
    stacks = [[crates[i][pos]
               for i in range(1, len(crates))
               if (len(crates[i]) > pos) and (crates[i][pos] != ' ')]
              for index, pos in index_positions.items()]
    return stacks


def perform_procedure(stacks, number, from_, to):
    stack_to_move = list(reversed(stacks[from_ - 1][-number:]))
    stacks[to - 1] = stacks[to - 1] + stack_to_move
    stacks[from_ - 1] = stacks[from_ - 1][:-number]


def perform_procedure_2(stacks, number, from_, to):
    stack_to_move = stacks[from_ - 1][-number:]
    stacks[to - 1] = stacks[to - 1] + stack_to_move
    stacks[from_ - 1] = stacks[from_ - 1][:-number]


def not_newline(line):
    return line != "\n"


def parse_procedure(line):
    return [int(i) for i in PROCEDURE_PATTERN.match(line).groups()]


if __name__ == "__main__":
    with open("input", "r") as text_input:
        input_lines = text_input.readlines()

    crates = list(itertools.takewhile(lambda x: x != "\n", input_lines))
    procedures = [parse_procedure(proc) for proc in
                  filter(not_newline, itertools.dropwhile(not_newline, input_lines))]
    stacks = process_crates(crates)
    stacks_2 = copy.deepcopy(stacks)
    [perform_procedure(stacks, *procedure) for procedure in procedures]
    print(f"Part 1: {''.join([stack[-1] for stack in stacks])}")
    [perform_procedure_2(stacks_2, *procedure) for procedure in procedures]
    print(f"Part 2: {''.join([stack[-1] for stack in stacks_2])}")
