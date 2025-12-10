def is_valid(id):
    for n in range(1, len(id)):
        pat = id[:n]

        i = n
        repeat = True
        while i < len(id):
            if pat != id[i : i + n]:
                repeat = False
                break

            i += n

        if repeat:
            print("%s -> %s" % (id, pat))
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
