SCORE_GUIDE = {
    "A X": 3,
    "A Y": 4,
    "A Z": 8,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 2,
    "C Y": 6,
    "C Z": 7,
}

if __name__ == "__main__":
    with open("input", "r") as text_input:
        input_lines = text_input.readlines()
        result = sum([SCORE_GUIDE[line.replace("\n", "")] for line in input_lines])
        print(result)
