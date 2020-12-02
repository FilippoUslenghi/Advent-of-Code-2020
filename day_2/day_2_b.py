with open("input.txt") as f:

    validPwds = 0
    for line in f:
        line = line.replace("-", " ")
        line = line.replace(":", "")
        line = line.split(" ")
        a, b, letter, pwd = line
        
        if (letter == pwd[int(a)-1]) ^ (letter == pwd[int(b)-1]):
            validPwds += 1

    print(validPwds)