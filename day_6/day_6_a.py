with open("input.txt", "a") as myfile:
    myfile.write("\n")

with open("input.txt") as f:

    sum = 0
    groupAnswer = set()
    s = set()

    for line in f:
        
        line = line[:-1]
        s = set(line)
        groupAnswer = groupAnswer.union(s)

        if len(line) == 0:
            sum += len(groupAnswer)
            groupAnswer = set()

    print(sum)
