if __name__ == "__main__":
    with open("input", "r") as input_file:
        input_lines = input_file.readlines()

    tree_height_array = [[int(sym) for sym in line[:-1]] for line in input_lines]
    rows = len(tree_height_array)
    columns = len(tree_height_array[0])
    visible = [[0 for i in range(columns)] for j in range(rows)]

    for i in range(rows):
        highest = -1
        for j in range(columns):
            current_tree = tree_height_array[i][j]
            if current_tree > highest:
                visible[i][j] = 1
                highest = current_tree

    for i in range(rows):
        highest = -1
        for j in range(columns - 1, -1, -1):
            current_tree = tree_height_array[i][j]
            if current_tree > highest:
                visible[i][j] = 1
                highest = current_tree

    for j in range(columns):
        highest = -1
        for i in range(rows):
            current_tree = tree_height_array[i][j]
            if current_tree > highest:
                visible[i][j] = 1
                highest = current_tree

    for j in range(columns):
        highest = -1
        for i in range(rows - 1, -1, -1):
            current_tree = tree_height_array[i][j]
            if current_tree > highest:
                visible[i][j] = 1
                highest = current_tree

    print('\n'.join([''.join([str(j) for j in i]) for i in visible]))
    res = sum([sum(i) for i in visible])
    print(res)
