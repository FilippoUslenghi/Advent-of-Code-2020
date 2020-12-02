with open("input.txt") as f:

    validPwds = 0
    for line in f:
        line = line.replace("-", " ")
        line = line.replace(":", "")
        line = line.split(" ")
        lower_limit, upper_limit, letter, pwd = line

        count = 0
        for char in pwd:
            if char == letter:
                count += 1

        if count >= int(lower_limit) and count <= int(upper_limit):
            validPwds += 1

    print(validPwds)