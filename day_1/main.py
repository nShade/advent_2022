def calculate_calories(calories):
    return 0


if __name__ == "__main__":
    with open("input", "r") as text_input:
        input_lines = text_input.readlines()
        result = calculate_calories(input_lines)
        print(result)
