def main():
    l = []

    with open("input.txt") as f:
        for line in f:
            l.append(int(line))

    for x in range(len(l)):
        for y in range(len(l[x:])):
            for z in l[y:]:
                if l[x] + l[y] + z == 2020:
                    return (l[x]*l[y]*z)

print(main())