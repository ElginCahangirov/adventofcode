from typing import Iterable


def main() -> int:
    input_data = parse_input()
    invalid_ids = []

    for rng in input_data:
        invalid_ids.extend(generate_invalid_ids(rng[0], rng[1]))

    return sum(invalid_ids)


def parse_input(input_file_path: str = "input.txt") -> list[tuple[str, str]]:
    with open(input_file_path, "r") as f:
        data = f.read().strip()

    result = []

    for rng in data.split(","):
        result.append(rng.split("-"))

    return result


def generate_invalid_ids(start: str, end: str) -> Iterable[int]:
    for start, end in split_range(start, end):
        start_int = int(start)
        end_int = int(end)
        found = set()

        for i in range(1, len(start) // 2 + 1):
            if len(start) % i != 0:
                continue

            seq = start[:i]

            while int(seq) < int(end[:i]) + 1:
                invalid_id_candidate = seq * (len(start) // i)
                invalid_id_candidate_int = int(invalid_id_candidate)

                if (
                    invalid_id_candidate_int >= start_int
                    and invalid_id_candidate_int <= end_int
                ):
                    if invalid_id_candidate not in found:
                        found.add(invalid_id_candidate)
                        yield invalid_id_candidate_int

                seq = str(int(seq) + 1)


def split_range(start: str, end: str) -> Iterable[tuple[str, str]]:
    diff = len(end) - len(start)
    dividers = [10 ** (len(start) + i) for i in range(diff)]

    for div in dividers:
        yield (str(start), str(div - 1))
        start = div

    yield (str(start), str(end))


if __name__ == "__main__":
    print(main())
