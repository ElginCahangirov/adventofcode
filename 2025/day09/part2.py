def main() -> int:
    input_data = parse_input()
    red_tiles = input_data_to_red_tiles(input_data)
    borders = calc_borders(red_tiles)
    # print_board(red_tiles, borders)
    largest_rect = find_largest_area(red_tiles, borders)
    return largest_rect


def parse_input(input_file_path: str = "input.txt") -> list[tuple[int, int]]:
    tiles = []

    with open(input_file_path, "r") as f:
        for line in f:
            line = line.strip()

            if not line:
                continue

            x, y = [int(n) for n in line.split(",")]
            tiles.append((x, y))

    return tiles


def input_data_to_red_tiles(input_data: list[tuple[int, int]]) -> list[tuple[int, int]]:
    return [(x, y) for (y, x) in input_data]


def calc_borders(red_tiles: list[tuple[int, int]]) -> set[tuple[int, int]]:
    borders = set()
    count = len(red_tiles)
    directions = [
        get_direction(red_tiles[i], red_tiles[(i + 1) % count]) for i in range(count)
    ]

    for i in range(count):
        tile = red_tiles[i]
        next_tile = red_tiles[(i + 1) % count]

        direction = directions[i]
        prev_direction = directions[i - 1]
        next_direction = directions[(i + 1) % count]

        start_ext = get_corner_extension(prev_direction, direction)
        end_ext = get_corner_extension(direction, next_direction)

        match direction:
            case ">":
                row = tile[0] - 1
                borders.update(
                    [
                        (row, y)
                        for y in range(tile[1] - start_ext, next_tile[1] + end_ext + 1)
                    ]
                )
            case "<":
                row = tile[0] + 1
                borders.update(
                    [
                        (row, y)
                        for y in range(next_tile[1] - end_ext, tile[1] + start_ext + 1)
                    ]
                )
            case "v":
                col = tile[1] + 1
                borders.update(
                    [
                        (x, col)
                        for x in range(tile[0] - start_ext, next_tile[0] + end_ext + 1)
                    ]
                )
            case "^":
                col = tile[1] - 1
                borders.update(
                    [
                        (x, col)
                        for x in range(next_tile[0] - end_ext, tile[0] + start_ext + 1)
                    ]
                )

    return borders


def get_direction(tile1: tuple[int, int], tile2: tuple[int, int]) -> str:
    if tile1[0] == tile2[0]:
        if tile1[1] > tile2[1]:
            return "<"
        else:
            return ">"
    else:
        if tile1[0] > tile2[0]:
            return "^"
        else:
            return "v"


def get_corner_extension(direction_in: str, direction_out: str) -> int:
    clockwise_turns = {(">", "v"), ("v", "<"), ("<", "^"), ("^", ">")}

    if (direction_in, direction_out) in clockwise_turns:
        return 1

    return -1


def find_largest_area_my(
    red_tiles: list[tuple[int, int]], borders: set[tuple[int, int]]
) -> int:
    largest_so_far = 0
    total = len(red_tiles) ** 2 // 2
    counter = 0

    for i in range(len(red_tiles)):
        for j in range(i + 1, len(red_tiles)):
            rectangle = build_rectangle(red_tiles[i], red_tiles[j])
            if walk_rectangle(rectangle, borders):
                area = calc_area(red_tiles[i], red_tiles[j])
                largest_so_far = max(largest_so_far, area)
            counter += 1
            if counter % 100 == 0:
                print(f"\r{counter}/{total}", end="")

    print()
    return largest_so_far


def find_largest_area(
    red_tiles: list[tuple[int, int]], borders: set[tuple[int, int]]
) -> int:
    pairs = []

    for i in range(len(red_tiles)):
        for j in range(i + 1, len(red_tiles)):
            pairs.append((red_tiles[i], red_tiles[j]))

    pairs.sort(key=lambda pair: calc_area(pair[0], pair[1]), reverse=True)
    total = len(pairs)

    for counter, (tile1, tile2) in enumerate(pairs, start=1):
        rectangle = build_rectangle(tile1, tile2)

        if walk_rectangle(rectangle, borders):
            print()
            return calc_area(tile1, tile2)

        if counter % 100 == 0:
            print(f"\r{counter}/{total}", end="")

    print()
    return 0


def build_rectangle(
    tile1: tuple[int, int], tile2: tuple[int, int]
) -> list[tuple[int, int]]:
    minrow = min(tile1[0], tile2[0])
    maxrow = max(tile1[0], tile2[0])
    mincol = min(tile1[1], tile2[1])
    maxcol = max(tile1[1], tile2[1])
    corner1 = (minrow, mincol)
    corner2 = (minrow, maxcol)
    corner3 = (maxrow, maxcol)
    corner4 = (maxrow, mincol)

    return [corner1, corner2, corner3, corner4]


def walk_rectangle(
    rectangle: list[tuple[int, int]], borders: set[tuple[int, int]]
) -> bool:
    top = min(row for row, col in rectangle)
    bottom = max(row for row, col in rectangle)
    left = min(col for row, col in rectangle)
    right = max(col for row, col in rectangle)

    for col in range(left, right + 1):
        if (top, col) in borders or (bottom, col) in borders:
            return False

    for row in range(top, bottom + 1):
        if (row, left) in borders or (row, right) in borders:
            return False

    return True


def calc_area(tile1: tuple[int, int], tile2: tuple[int, int]) -> int:
    width = abs(tile1[0] - tile2[0]) + 1
    height = abs(tile1[1] - tile2[1]) + 1
    return width * height


def print_board(
    red_tiles: list[tuple[int, int]], borders: set[tuple[int, int]]
) -> None:
    max_row = max(tile[0] for tile in red_tiles)
    max_col = max(tile[1] for tile in red_tiles)
    red_tiles_map = set(red_tiles)

    for i in range(max_row + 2):
        for j in range(max_col + 3):
            if (i, j) in red_tiles_map:
                print("#", end="")
            elif (i, j) in borders:
                print("0", end="")
            else:
                print(".", end="")
        print()


if __name__ == "__main__":
    print(main())
