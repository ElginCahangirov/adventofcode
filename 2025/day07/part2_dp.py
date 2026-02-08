def main() -> int:
    input_data = parse_input()
    start = input_data["start"]
    grid = input_data["grid"]

    return count_paths(grid, start)


def parse_input(input_file_path: str = "input.txt") -> dict:
    with open(input_file_path, "r") as f:
        grid = []
        start = None
        row = 0

        for line in f:
            line = line.strip()
            col = 0
            line_data = []

            for ch in line:
                line_data.append(ch)

                if ch == "S":
                    start = (row, col)

                col += 1

            row += 1

            if line_data:
                grid.append(line_data)

    return {"grid": grid, "start": start}


def count_paths(grid: list[list[str]], start: tuple[int, int]) -> int:
    rows = len(grid)
    cols = len(grid[0])
    start_row, start_col = start
    dp = [1] * cols

    for r in range(rows - 2, start_row - 1, -1):
        new_dp = [0] * cols

        for c in range(cols):
            cell_below = grid[r + 1][c]

            if cell_below == "^":
                left_paths = dp[c - 1]
                right_paths = dp[c + 1]
                new_dp[c] = left_paths + right_paths
            else:
                new_dp[c] = dp[c]

        dp = new_dp

    return dp[start_col]


if __name__ == "__main__":
    print(main())
