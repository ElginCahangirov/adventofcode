def main() -> int:
    input_data = parse_input()
    loc = 50
    password = 0

    for rotation in input_data:
        loc = rotate(loc, rotation)

        if loc == 0:
            password += 1

    return password


def parse_input(input_file_path: str = "input.txt") -> list[str]:
    with open(input_file_path, "r") as f:
        return f.read().splitlines()


def rotate(start: int, rotation: str) -> int:
    direction, distance = rotation[0], int(rotation[1:])
    distance %= 100

    match direction:
        case "L":
            dest = start - distance
        case "R":
            dest = start + distance

    if dest < 0:
        dest += 100
    elif dest > 99:
        dest -= 100

    return dest


if __name__ == "__main__":
    print(main())
