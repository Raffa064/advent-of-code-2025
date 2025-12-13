import re

with open("input.txt") as file:
    input = [re.split(" +", x.strip()) for x in file.readlines()]

    op = input[-1]
    matrix = [[int(x) for x in row] for row in input[:-1]]
    results = [0 if x == "+" else 1 for x in input[-1]]

    for i in range(len(matrix)):
        row = matrix[i]

        print("[ row %d ]" % (i + 1))

        for j in range(len(results)):
            print("  \033[32m", results[j], "\033[0m", op[j], row[j])

            match op[j]:
                case "+":
                    results[j] += row[j]
                case "*":
                    results[j] *= row[j]

    print("\nResults: ", results)

    print("Sum of results: ", sum(results))
