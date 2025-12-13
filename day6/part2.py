from functools import reduce


with open("input.txt") as file:
    grid = [list(x.replace("\n", "")) for x in file.readlines()]

    width = len(grid[0])
    height = len(grid)

    print("input %dx%d" % (width, height))

    stack = []
    acc = 0
    for x in range(width - 1, -1, -1):
        num = ""
        for y in range(height):
            num += grid[y][x]

        op = num[-1]
        num = num[:-1].strip()  # remove ws/op

        if num:
            print("Push: ", num)
            stack.append(int(num))

            if op == "+":
                acc += sum(stack)
            elif op == "*":
                acc += reduce(lambda p, c: p * c, stack, 1)
            else:
                continue

            print("Acc: ", op)
            stack.clear()

    print("Result: ", acc)
