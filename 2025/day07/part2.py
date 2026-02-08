from functools import lru_cache


def main() -> int:
    input_data = parse_input()
    timelines = []
    start = input_data["start"]
    grid = input_data["grid"]
    # walk(grid, start, [], timelines)
    return walk(grid, start)


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

    return {"grid": tuple([tuple(l) for l in grid]), "start": start}


@lru_cache
def walk(
    grid: tuple[tuple[str]],
    pos: tuple[int, int],
) -> None:
    if pos is None:
        return 0

    down = move(grid, pos, "down")

    if down is None:
        return 1 + walk(grid, down)

    row, col = down

    if grid[row][col] == "^":
        left = move(grid, down, "left")
        right = move(grid, down, "right")
        return walk(grid, right) + walk(grid, left)
    else:
        return walk(grid, down)


def move(
    grid: tuple[tuple[str]], start: tuple[int, int], direction: str
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


def is_within(grid: tuple[tuple[str]], pos: tuple[int, int]) -> bool:
    max_row, max_col = len(grid), len(grid[0])
    row, col = pos

    return 0 <= row < max_row and 0 <= col < max_col


if __name__ == "__main__":
    print(main())
