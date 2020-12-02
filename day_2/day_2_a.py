with open("input.txt") as f:

    validPwds = 0
    iterations = 1
    for line in f:
        policy = line.split(":")[0]
        pwd = line.split(":")[1][1:-1]
        limits = policy.split(" ")[0]
        letter = policy.split(" ")[1]
        lower_limit = int(min(limits.split("-")))
        upper_limit = int(max(limits.split("-")))

        count = 0
        for char in pwd:
            if char == letter:
                count += 1

        if count >= lower_limit and count <= upper_limit:
            validPwds += 1

        # if iterations == 8:
        #     print(line[:-1])
        #     break

        # iterations += 1

    print(validPwds)
