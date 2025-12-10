with open("input.txt", "r") as file:
    output_joltage = 0
    for bank in file.readlines():
        bank = bank.strip()

        digits = list(bank)

        for i in range(len(bank) - 12):
            for j in range(len(digits) - 1):
                if digits[j] < digits[j + 1]:
                    digits.pop(j)
                    break

        bank_joltage = int(str.join("", digits[:12]))

        print(bank_joltage)

        output_joltage += bank_joltage

    print("Output joltage: ", output_joltage)
