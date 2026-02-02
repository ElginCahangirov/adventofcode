def main() -> int:
    input_data = parse_input()
    total = calc_total(input_data)
    return total


def parse_input(input_file_path: str = "input.txt") -> list[list[str | int]]:
    data = []

    with open(input_file_path, "r") as f:
        for line in f:
            line_data = line.split()

            if line_data:
                if line_data[0].isdigit():
                    line_data = [int(n) for n in line_data]

                data.append(line_data)

    return data


def calc_total(data: list[list[str | int]]) -> int:
    nrows = len(data)
    ncols = len(data[0])
    total = 0

    for j in range(ncols):
        op = data[nrows - 1][j]

        match op:
            case "+":
                col_result = 0
            case "*":
                col_result = 1

        for i in range(nrows - 1):
            match op:
                case "+":
                    col_result += data[i][j]
                case "*":
                    col_result *= data[i][j]

        total += col_result

    return total


if __name__ == "__main__":
    print(main())
