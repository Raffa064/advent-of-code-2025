with open("input.txt", "r") as file:
    fresh_ranges = []

    for line in file.readlines():
        line = line.strip()

        if line == "":
            break
        else:
            fresh = [int(x) for x in line.split("-")]
            fresh_ranges.append(fresh)

    fresh_ranges.sort()

    count = 0
    last = fresh_ranges[0]
    for lo, hi in fresh_ranges[1:]:
        if last[1] >= lo:
            last = (last[0], max(last[1], hi))  # merge if overlaps
        else:
            count += last[1] - last[0] + 1
            last = (lo, hi)

    count += last[1] - last[0] + 1

    print("Count: ", count)
