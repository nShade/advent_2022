def find_marker(input):
    """
    >>> find_marker("abcd")
    4
    >>> find_marker("abcbde")
    6
    """
    last_three = input[:3]

    for i, letter in enumerate(input[3:]):

        if len(set(last_three + letter)) == 4:
            return i + 4

        last_three = last_three[-2:] + letter

    return -1

if __name__ == "__main__":
    with open("input", "r") as text_input:
        input = text_input.read()

    print(find_marker(input))
