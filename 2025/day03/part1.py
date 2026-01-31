def main() -> int:
    input_data = parse_input()
    total_joltage = 0

    for bank in input_data:
        total_joltage += calc_max_joltage(bank)

    return total_joltage


def parse_input(input_file_path: str = "input.txt") -> list[list[int]]:
    input_data = []

    with open(input_file_path, "r") as f:
        for line in f:
            row = [int(x) for x in list(line.strip())]

            if row:
                input_data.append(row)

    return input_data


def calc_max_joltage(bank: list[int]) -> int:
    first_max = 0
    second_max = 0

    for ind, power in enumerate(bank):
        if ind != len(bank) - 1 and power > first_max:
            first_max = power
            second_max = 0
        elif power > second_max:
            second_max = power

    return first_max * 10 + second_max


if __name__ == "__main__":
    print(main())
