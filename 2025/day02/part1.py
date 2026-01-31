from typing import Iterable


def main() -> int:
    input_data = parse_input()
    invalid_ids = []

    for rng in input_data:
        invalid_ids.extend(get_invalid_ids(rng))

    return sum(invalid_ids)


def parse_input(input_file_path: str = "input.txt") -> list[tuple[str, str]]:
    with open(input_file_path, "r") as f:
        data = f.read().strip()

    result = []

    for rng in data.split(","):
        result.append(rng.split("-"))

    return result


def get_invalid_ids(rng: tuple[str, str]) -> list[int]:
    rng_start, rng_end = int(rng[0]), int(rng[1])
    rng_digits_lens = {len(digit) for digit in rng}
    invalid_ids = []

    for digit_len in rng_digits_lens:
        if digit_len % 2:
            continue

        all_invalid_ids = generate_invalid_ids(digit_len)
        invalid_ids_in_range = list(
            filter(lambda x: rng_start <= x <= rng_end, all_invalid_ids)
        )
        invalid_ids.extend(invalid_ids_in_range)

    return invalid_ids


def generate_invalid_ids(n: int) -> Iterable[int]:
    for i in range(10 ** (n // 2 - 1), 10 ** (n // 2)):
        yield i * 10 ** (n // 2) + i


if __name__ == "__main__":
    print(main())
