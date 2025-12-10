READ_RANGES = 0
READ_INGREDIENTS = 1

with open("input.txt", "r") as file:
    fresh_ranges = []
    ingredients = []

    state = READ_RANGES
    for line in file.readlines():
        line = line.strip()

        if line == "":
            state = READ_INGREDIENTS
        elif state == READ_RANGES:
            fresh = [int(x) for x in line.split("-")]
            fresh_ranges.append(fresh)
        else:
            id = int(line)
            ingredients.append(id)

    fresh_count = 0
    for i in ingredients:
        for min_, max_ in fresh_ranges:
            if i >= min_ and i <= max_:
                fresh_count += 1
                break

    print("Fresh ingridient count: ", fresh_count)
