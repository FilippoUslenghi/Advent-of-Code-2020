import string

with open("input.txt", "a") as myfile:
    myfile.write("\n")

with open("input.txt") as f:

    sum = 0
    groupAnswer = set(string.ascii_lowercase)
    s = set()

    for line in f:
        line = line[:-1]
        
        if bool(line) == False:
            sum += len(groupAnswer)
            groupAnswer = set(string.ascii_lowercase)
            continue

        s = set(line)
        groupAnswer = groupAnswer.intersection(s)

    print(sum)
 