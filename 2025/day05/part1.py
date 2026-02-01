def main() -> int:
    ranges, ingredients = parse_input()
    ingredients.sort()
    ranges = merge_overlapping_ranges(ranges)
    result = count_fresh(ranges, ingredients)

    return result


def count_fresh(ranges: list[tuple[int, int]], ingredients: list[int]) -> int:
    range_pointer = 0
    ingredient_pointer = 0
    freshes = 0

    while True:
        if range_pointer == len(ranges) or ingredient_pointer == len(ingredients):
            break

        curr_range = ranges[range_pointer]
        rng_start, rng_end = curr_range
        ingredient = ingredients[ingredient_pointer]

        if ingredient < rng_start:
            ingredient_pointer += 1
        elif rng_start <= ingredient <= rng_end:
            freshes += 1
            ingredient_pointer += 1
        else:
            range_pointer += 1

    return freshes


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
) -> tuple[list[tuple[int, int]], list[int]]:
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
                if line:
                    ingredients.append(int(line))

    return ranges, ingredients


if __name__ == "__main__":
    print(main())
