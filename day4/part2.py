neighbor = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]


def count_accessible_rolls(input):
    output = [x[:] for x in input]

    width = len(input[0])
    height = len(input)

    accessible = 0
    for y in range(height):
        for x in range(width):
            if input[y][x] == "@":
                rolls = 0
                for u, v in neighbor:
                    w = x + u
                    k = y + v

                    if w < 0 or w >= width:
                        continue

                    if k < 0 or k >= height:
                        continue

                    if input[k][w] == "@":
                        rolls += 1

                if rolls < 4:
                    accessible += 1
                    output[y][x] = "\033[31mx\033[0m"

            print(output[y][x], end="")
        print()

    return output, accessible


with open("input.txt", "r") as file:
    grid = [list(x.strip()) for x in file.readlines()]

    total = 0
    while True:
        grid, accessible = count_accessible_rolls(grid)
        print("Remove %d rolls of paper" % accessible)

        if accessible == 0:
            break

        total += accessible

    print("Accessible rolls: ", total)
