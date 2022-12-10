def run_cycles(input_lines):
    register = 1

    for line in input_lines:
        yield register

        if line.startswith('addx'):
            yield register
            register += int(line[5:])


if __name__ == "__main__":
    with open("input", "r") as input_file:
        input_lines = input_file.readlines()

    registers = list(run_cycles(input_lines))
    res_1 = sum([registers[cycle - 1] * cycle for cycle in range(20, 240, 40)])
    print(f"Part 1: {res_1}")
    screen = ["#"
              if register - 1 <= pixel % 40 <= register + 1
              else "."
              for pixel, register in enumerate(registers)]
    res_2 = '\n'.join([''.join(screen[i * 40:(i + 1) * 40]) for i in range(6)])
    print("Part 2:")
    print(res_2)
   