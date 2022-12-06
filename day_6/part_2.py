def find_marker(input):
    last_three = input[:13]

    for i, letter in enumerate(input[13:]):

        if len(set(last_three + letter)) == 14:
            return i + 14

        last_three = last_three[-12:] + letter

    return -1

if __name__ == "__main__":
    with open("input", "r") as text_input:
        input = text_input.read()

    print(find_marker(input))
