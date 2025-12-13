from functools import lru_cache

grid: list


@lru_cache(None)
def count_timelines(x, y):
    global grid

    if y >= len(grid):
        return 1

    if grid[y][x] == "^":
        return (
            count_timelines(x - 1, y + 1)  #
            + count_timelines(x + 1, y + 1)  #
        )

    return count_timelines(x, y + 1)


with open("input.txt") as file:
    grid = [list(x) for x in file.readlines()]

    x = grid[0].index("S")
    timeline_count = count_timelines(x, 0)

    print("Timeline count: ", timeline_count)
