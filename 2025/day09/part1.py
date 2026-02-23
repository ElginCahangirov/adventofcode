def main() -> int:
    input_data = parse_input()
    largest_rect = find_largest_area(input_data)
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


def find_largest_area(tiles: list[tuple[int, int]]) -> int:
    largest_so_far = 0

    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            area = calc_area(tiles[i], tiles[j])
            largest_so_far = max(largest_so_far, area)

    return largest_so_far


def calc_area(tile1: tuple[int, int], tile2: tuple[int, int]) -> int:
    width = abs(tile1[0] - tile2[0]) + 1
    height = abs(tile1[1] - tile2[1]) + 1
    return width * height


if __name__ == "__main__":
    print(main())
