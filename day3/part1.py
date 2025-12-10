with open("input.txt", "r") as file:
    output_joltage = 0
    for bank in file.readlines():
        bank = bank.strip()
        max_joltage = 0

        for i in range(0, len(bank)):
            for j in range(i + 1, len(bank)):
                curr_joltage = int(bank[i]) * 10 + int(bank[j])
                max_joltage = max(max_joltage, curr_joltage)

        print("%s J: %d" % (bank, max_joltage))
        output_joltage += max_joltage

    print(output_joltage)
