SCORE_GUIDE_1 = {
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

SCORE_GUIDE_2 = {
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
        result_1 = sum([SCORE_GUIDE_1[line[:-1]] for line in input_lines])
        print(f"Part 1: {result_1}")
        result_2 = sum([SCORE_GUIDE_2[line[:-1]] for line in input_lines])
        print(f"Part 2: {result_2}")
