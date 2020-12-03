with open("input.txt") as f:

    i = 0
    trees = 0
    for line in f:
        line = line[:-1]
        i = (i + 3) % len(line)
        if line[i] == "#":
            trees += 1
            print(i)
    print("Trees encountered: " + str(trees))
