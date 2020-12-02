with open("input.txt") as f:

    validPwds = 0
    for line in f:
        policy = line.split(":")[0]
        pwd = line.split(":")[1][1:-1]
        limits = policy.split(" ")[0]
        letter = policy.split(" ")[1]
        lower_limit = int(limits.split("-")[0])
        upper_limit = int(limits.split("-")[1])

        count = 0
        for char in pwd:
            if char == letter:
                count += 1

        if count >= lower_limit and count <= upper_limit:
            validPwds += 1

    print(validPwds)