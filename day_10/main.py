import itertools


def process_command(line):
    if line[:4] == 'noop':
        return 'noop', None
    else:
        return 'addx', int(line[5:])


def execute_command(command, register):
    cmd, arg = command
    if cmd == "noop":
        return register
    if cmd == "addx":
        return register + arg
    return register


def run_cycle(command_cache, input_lines, register):
    if command_cache:
        command = command_cache
        command_cache = None
    else:
        command = process_command(next(input_lines))
        if command[0] == 'addx':
            command_cache = command
            command = None, None

    register = execute_command(command, register)
    return command_cache, register


def run_cycles(input_lines):
    command_cache = None
    register = 1
    while True:
        try:
            command_cache, register = run_cycle(command_cache, input_lines, register)
            yield register
        except StopIteration:
            return


if __name__ == "__main__":
    with open("input", "r") as input_file:
        input_lines = iter(input_file.readlines())

    registers = list(run_cycles(input_lines))
    res_1 = sum([registers[cycle - 2] * cycle for cycle in range(20, 240, 40)])
    print(f"Part 1: {res_1}")