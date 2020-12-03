with open("input.txt") as f:

    i = 0
    trees = 0
    for line in f:
        line = line[:-1]
        if line[i % len(line)] == "#":
            trees += 1
        i = i + 3
    print("Trees encountered: " + str(trees))
