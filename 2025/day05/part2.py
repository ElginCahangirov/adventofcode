def main() -> int:
    ranges = parse_input()
    ranges = merge_overlapping_ranges(ranges)
    count = 0

    for rng in ranges:
        count += rng[1] - rng[0] + 1

    return count


def merge_overlapping_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    ranges.sort()
    merged_ranges = []

    for i in range(1, len(ranges)):
        rng = ranges[i]
        prev_rng = ranges[i - 1]

        if rng[0] > prev_rng[1]:
            continue

        merged_rng = prev_rng[0], max(rng[1], prev_rng[1])
        ranges[i - 1] = merged_rng
        ranges[i] = merged_rng

    for i in range(1, len(ranges)):
        if ranges[i][0] != ranges[i - 1][0]:
            merged_ranges.append(ranges[i - 1])

    merged_ranges.append(ranges[i])

    return merged_ranges


def parse_input(
    input_file_path: str = "input.txt",
    parse_ingredients: bool = False,
) -> tuple[list[tuple[int, int]], list[int]] | list[tuple[int, int]]:
    ranges = []
    ingredients = []
    section = "ranges"

    with open(input_file_path, "r") as f:
        for line in f:
            line = line.strip()

            if not line:
                section = "ingredients"

            if section == "ranges":
                start, end = line.split("-")
                ranges.append((int(start), int(end)))

            if section == "ingredients":
                if not parse_ingredients:
                    break

                if line:
                    ingredients.append(int(line))

    if parse_ingredients:
        return ranges, ingredients
    else:
        return ranges


if __name__ == "__main__":
    print(main())
