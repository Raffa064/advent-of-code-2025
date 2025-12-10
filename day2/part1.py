def is_valid(id):
    split = len(id) // 2
    left = id[:split]
    right = id[split:]

    if left == right:
        print(id, left, right)
        return False

    return True


with open("input.txt", "r") as file:
    content = file.read()

    sum = 0
    for str_range in content.split(","):
        (start, end) = [int(x) for x in str_range.split("-")]

        for n in range(start, end + 1):
            id = str(n)
            if not is_valid(id):
                sum += n

    print("Total sum: ", sum)
