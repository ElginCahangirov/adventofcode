from typing import Iterable


def main() -> int:
    input_data = parse_input()
    total = 0

    while (count := get_accessible_papers(input_data)) > 0:
        total += count

    return total


def parse_input(input_file_path: str = "input.txt") -> list[list[str]]:
    input_data = []

    with open(input_file_path, "r") as f:
        for line in f:
            if line.strip():
                input_data.append(list(line.strip()))

    return input_data


def get_accessible_papers(diagram: list[list[str]]) -> int:
    count = 0

    for row in range(len(diagram)):
        for col in range(len(diagram[0])):
            if diagram[row][col] == "@":
                if get_adjacent_papers_cnt(diagram, row, col) < 4:
                    diagram[row][col] = "x"
                    count += 1

    return count


def get_adjacent_papers_cnt(diagram: list[list[str]], row: int, col: int) -> int:
    count = 0

    for i, j in get_adjacent_positions(diagram, row, col):
        if diagram[i][j] == "@":
            count += 1

    return count


def get_adjacent_positions(
    diagram: list[list[str]], row: int, col: int
) -> Iterable[tuple[int, int]]:
    row_min = col_min = 0
    row_max = len(diagram) - 1
    col_max = len(diagram[0]) - 1

    def _candidates() -> Iterable[tuple[int, int]]:
        yield row - 1, col - 1
        yield row - 1, col
        yield row - 1, col + 1
        yield row, col - 1
        yield row, col + 1
        yield row + 1, col - 1
        yield row + 1, col
        yield row + 1, col + 1

    def _candidate_is_in_range(row: int, col: int) -> bool:
        return row_min <= row <= row_max and col_min <= col <= col_max

    for i, j in _candidates():
        if _candidate_is_in_range(i, j):
            yield i, j


if __name__ == "__main__":
    print(main())
