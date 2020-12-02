with open("input.txt") as f:

    validPwds = 0
    for line in f:
        line = line.replace("-", " ")
        line = line.replace(":", "")
        line = line.split(" ")
        first_position, second_position, letter, pwd = line
        
        if (letter == pwd[int(first_position)-1]) ^ (letter == pwd[int(second_position)-1]):
            validPwds += 1

    print(validPwds)