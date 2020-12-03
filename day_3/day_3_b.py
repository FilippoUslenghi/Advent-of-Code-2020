def firstSlopes(x):
    i = 0
    trees = 0
    for line in f:
        line = line[:-1]
        if line[i % len(line)] == "#":
            trees += 1
        i = i + x
    return(trees)


def lastSlope():
    i = 0
    trees = 0
    for line in f:
        line = line[:-1]
        if line[i % len(line)] == "#":
            trees += 1
        i = i + 1
        f.readline()
    return(trees)


with open("input.txt") as f:
    first = firstSlopes(1)
    print("first:", first)
    f.seek(0, 0)
    second = firstSlopes(3)
    print("second:", second)
    f.seek(0, 0)
    third = firstSlopes(5)
    print("third:", third)
    f.seek(0, 0)
    fourth = firstSlopes(7)
    print("fourth:", fourth)
    f.seek(0, 0)
    fifth = lastSlope()
    print("fifth:", fifth)
    print("result:", first*second*third*fourth*fifth)
