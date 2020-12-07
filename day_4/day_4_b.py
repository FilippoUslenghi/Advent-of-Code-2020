import re

with open("input.txt", "a") as myfile:
    myfile.write("\n")

with open("input.txt") as f:
    passport = ""
    patterns = ["byr:(19[2-9]\\d( |\n)|200[0-2]( |\n))", "iyr:201\\d( |\n)|2020( |\n)", "eyr:202\\d( |\n)|2030( |\n)", "hgt:((1[5-8]\\d|19[0-3])cm( |\n)|(59|6\\d|7[0-6])in( |\n))", "hcl:#(\\d|[a-f]){6}( |\n)", "ecl:(amb|blu|brn|gry|grn|hzl|oth){1}( |\n)", "pid:\\d{9}( |\n)"]
    count = 0
    for line in f:
        passport += line
        if line == "\n":
            matches = []
            for pattern in patterns:
                matches.append(re.search(pattern, passport))
            if all(matches):
                count += 1
            passport = ""
    print(count)
