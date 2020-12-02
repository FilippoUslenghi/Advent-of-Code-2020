with open("input.txt") as f:

    validPwds = 0
    for line in f:
        policy = line.split(":")[0]
        pwd = line.split(":")[1][1:-1]
        limits = policy.split(" ")[0]
        letter = policy.split(" ")[1]
        a = int(limits.split("-")[0])
        b = int(limits.split("-")[1])

        if (letter == pwd[a-1]) ^ (letter == pwd[b-1]):
            validPwds += 1

    print(validPwds)