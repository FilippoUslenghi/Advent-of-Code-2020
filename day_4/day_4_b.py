import re

with open("input.txt", "a") as myfile:
    myfile.write("\n")

with open("input.txt") as f:
    passport = ""
    patterns = ["byr:(19[2-9]\\d|200[0-2])", "iyr:201\\d|2020", "eyr:202\\d|2030", "hgt:((1[5-8]\\d|19[0-3])cm|(59|6\\d|7[0-6])in)", "hcl:#(\\d|[a-f]){6}", "ecl:(amb|blu|brn|gry|grn|hzl|oth){1}", "pid:\\d{9}"]
    count = 0
    for line in f:
        passport += line
        if line == "\n":
            matches = []
            for pattern in patterns:
                pattern += "( |\n)"
                matches.append(re.search(pattern, passport))
            if all(matches):
                count += 1
            passport = ""
    print(count)
