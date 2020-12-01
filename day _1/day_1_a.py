def main():
    l = []

    with open("input.txt") as f:
        for line in f:
            l.append(int(line))

    for x in range(len(l)):
        for y in l[x:]:
            if l[x] + y == 2020:
                return (l[x]*y)

print(main())