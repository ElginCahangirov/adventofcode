def main() -> int:
    input_data = parse_input()
    total_joltage = 0

    for bank in input_data:
        total_joltage += int(calc_max_joltage(bank))

    return total_joltage


def parse_input(input_file_path: str = "input.txt") -> list[str]:
    input_data = []

    with open(input_file_path, "r") as f:
        for line in f:
            if line.strip():
                input_data.append(line.strip())

    return input_data


def calc_max_joltage(bank: str) -> str:
    start = 0
    end = -11
    max_joltage = ""

    for i in range(12):
        current_max = max(bank[start:end])
        max_joltage += current_max
        start = bank[start:end].index(current_max) + start + 1
        end = (end + 1) or len(bank)

    return max_joltage


if __name__ == "__main__":
    print(main())
