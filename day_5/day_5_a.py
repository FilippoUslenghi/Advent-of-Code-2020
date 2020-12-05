with open("input.txt") as f:

    higherID = float('-inf')
    for line in f:
        rows = [n for n in range(128)]
        columns = [n for n in range(8)]
        for char in line[:7]:
            if char == "F":
                rows = rows[:(len(rows)//2)]
            else:
                rows = rows[len(rows)//2:]
        row = rows[0]

        for char in line[7:]:
            if char == "L":
                columns = columns[:(len(columns)//2)]
            else:
                columns = columns[(len(columns)//2):]
        column = columns[0]

        ID = row * 8 + column
        higherID = ID if ID > higherID else higherID

    print(higherID)
