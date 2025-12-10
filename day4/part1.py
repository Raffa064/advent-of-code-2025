neighbor = [
    [-1, +0],  # left
    [-1, +1],  # top-left
    [+0, +1],  # top
    [+1, +1],  # top-right
    [+1, +0],  # right
    [+1, -1],  # bottom-right
    [+0, -1],  # bottom
    [-1, -1],  # bottom-left
]

with open("input.txt", "r") as file:
    grid = file.readlines()
    accessible = 0

    width = len(grid[0])
    height = len(grid)

    for y in range(height):
        line = grid[y].strip()
        for x in range(width - 1):
            if grid[y][x] == "@":
                rolls = 0
                for u, v in neighbor:
                    w = x + u
                    k = y + v

                    if w < 0 or w >= width:
                        continue

                    if k < 0 or k >= height:
                        continue

                    if grid[k][w] == "@":
                        rolls += 1

                if rolls < 4:
                    accessible += 1
                    print("\033[31mx\033[0m", end="")
                else:
                    print(grid[y][x], end="")
            else:
                print(grid[y][x], end="")
        print()

    print("Accessible rolls: ", accessible)
