def main() -> int:
    input_data = parse_input()
    total = calc_total(input_data)
    return total


def parse_input(input_file_path: str = "input.txt") -> list[str]:
    with open(input_file_path, "r") as f:
        return [l for l in f.read().split("\n") if l]


def calc_total(data: list[str]) -> int:
    nrows = len(data)
    ncols = len(data[0])
    total = 0
    ops = data[nrows - 1]
    ops = fill_empty_ops(ops)
    col_values = []

    for j in range(ncols):
        op = ops[j]
        col_val = ""

        for i in range(nrows - 1):
            ch = data[i][j]

            if ch != " ":
                col_val += ch

        if col_val:
            col_values.append(int(col_val))
        else:
            total += calc_col_result(col_values, op)
            col_values.clear()

    total += calc_col_result(col_values, op)

    return total


def calc_col_result(values: int, op: str) -> int:
    match op:
        case "+":
            col_result = 0
        case "*":
            col_result = 1

    for val in values:
        match op:
            case "+":
                col_result += val
            case "*":
                col_result *= val

    return col_result


def fill_empty_ops(ops: str) -> list[str]:
    last_op = ""
    result = []

    for i, op in enumerate(ops):
        if op != " ":
            last_op = op

        result.append(last_op)

    return result


if __name__ == "__main__":
    print(main())
