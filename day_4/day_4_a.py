import re

with open("input.txt", "a") as myfile:
    myfile.write("\n")


with open("input.txt") as f:
    passport = ""
    patterns = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
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
