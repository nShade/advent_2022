SCORE_GUIDE = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6,
}

if __name__ == "__main__":
    with open("input", "r") as text_input:
        input_lines = text_input.readlines()
        result = sum([SCORE_GUIDE[line.replace("\n", "")] for line in input_lines])
        print(result)
