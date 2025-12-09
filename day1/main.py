with open("input.txt", "r") as file:
    offset = 50
    passwd = 0

    for line in file.readlines():
        line = line.strip()
        print(line, line[0], int(line[1:]))

        match line[0]:
            case "L":
                offset -= int(line[1:])
            case "R":
                offset += int(line[1:])

        offset = offset % 100

        if offset < 0:
            offset = 100 - offset

        if offset == 0:
            passwd += 1

    print("Passwd is: ", passwd)
