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


def process_procedure(procedure):
    return [int(x) for x in PROCEDURE_PATTERN.match(procedure).groups()]


def perform_procedure(stacks, procedure):
    number, from_, to = procedure
    stack_to_move = stacks[from_ - 1][-number:]
    stacks[to - 1] = stacks[to - 1] + stack_to_move
    stacks[from_ - 1] = stacks[from_ - 1][:-number]


if __name__ == "__main__":
    with open("input", "r") as text_input:
        input_lines = text_input.readlines()

    crates = list(itertools.takewhile(lambda x: x != "\n", input_lines))
    procedures = itertools.dropwhile(lambda x: x != "\n", input_lines)
    stacks = process_crates(crates)
    [perform_procedure(stacks, process_procedure(procedure)) for procedure in procedures if procedure != "\n"]
    print(''.join([stack[-1] for stack in stacks]))
