with open("input.txt") as f:

    i = 0
    count = 0
    for line in f:
        line = line[:-1]
        i = (i + 3) % len(line)
        if line[i] == "#":
            count += 1
    print(count)
