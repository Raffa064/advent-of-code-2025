with open("input.txt") as file:
    grid = [list(x) for x in file.readlines()]

    split_count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            match grid[i][j]:
                case ".":
                    if grid[i - 1][j] == "S" or grid[i - 1][j] == "|":
                        grid[i][j] = "|"
                case "^":
                    if grid[i - 1][j] == "|":
                        grid[i][j - 1] = "|"
                        grid[i][j + 1] = "|"
                        split_count += 1

    print(str.join("", [str.join("", x) for x in grid]))
    print("Split count: ", split_count)
