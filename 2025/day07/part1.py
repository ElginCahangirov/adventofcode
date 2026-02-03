def main() -> int:
    input_data = parse_input()
    splits_cnt = count_splits(input_data)
    return splits_cnt


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


def count_splits(data: dict) -> int:
    grid = data["grid"]
    start = data["start"]
    queue = [start]
    nrows, ncols = len(grid), len(grid[0])
    splits = 0
    visited = set()

    while queue:
        curr_pos = queue.pop()

        if curr_pos in visited:
            continue

        visited.add(curr_pos)
        row, col = curr_pos
        down = move(grid, (row, col), "down")

        if down is None:
            continue

        if grid[down[0]][down[1]] == "^":
            left = move(grid, down, "left")
            right = move(grid, down, "right")
            splits += 1
            queue.append(left)
            queue.append(right)
        else:
            queue.append(down)

    return splits


def move(
    grid: list[list[str]], start: tuple[int, int], direction: str
) -> tuple[int, int] | None:
    row, col = start

    match direction:
        case "down":
            row, col = row + 1, col
        case "up":
            row, col = row - 1, col
        case "left":
            row, col = row, col - 1
        case "right":
            row, col = row, col + 1

    pos = (row, col)

    if is_within(grid, pos):
        return pos


def is_within(grid: list[list[str]], pos: tuple[int, int]) -> bool:
    max_row, max_col = len(grid), len(grid[0])
    row, col = pos

    return 0 <= row < max_row and 0 <= col < max_col


if __name__ == "__main__":
    print(main())
