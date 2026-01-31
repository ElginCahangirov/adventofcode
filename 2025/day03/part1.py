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
    max_exclude_last = max(bank[:-1])
    max_exclude_last_index = bank.index(max_exclude_last)
    max_after_first = max(bank[(max_exclude_last_index + 1) :])
    return max_exclude_last * 10 + max_after_first


if __name__ == "__main__":
    print(main())
