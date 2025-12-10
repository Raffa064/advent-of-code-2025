colors = {
    "L": "\033[31m",  #
    "R": "\033[34m",  #
}

with open("input.txt", "r") as file:
    offset = 50
    passwd = 0

    for line in file.readlines():
        line = line.strip()
        dir = line[0]
        step = int(line[1:])

        print("% 8s %s%s \033[33m%d\033[0m" % (line, colors[dir], dir, step))

        for i in range(step):
            match dir:
                case "L":
                    offset -= 1
                case "R":
                    offset += 1

            if offset % 100 == 0:
                passwd += 1

    print("Passwd is: ", passwd)
