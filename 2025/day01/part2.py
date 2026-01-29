def main() -> int:
    input_data = parse_input()
    loc = 50
    password = 0

    for rotation in input_data:
        loc, times_crossed = rotate(loc, rotation)
        password += times_crossed

        if loc == 0:
            password += 1

    return password


def parse_input(input_file_path: str = "input.txt") -> list[str]:
    with open(input_file_path, "r") as f:
        return f.read().splitlines()


def rotate(start: int, rotation: str) -> tuple[int, int]:
    direction, distance = rotation[0], int(rotation[1:])
    cross_cnt = distance // 100
    distance %= 100

    match direction:
        case "L":
            dest = start - distance
        case "R":
            dest = start + distance

    if dest < 0:
        dest += 100
        if start != 0 and dest != 0:
            cross_cnt += 1
    elif dest > 99:
        dest -= 100
        if start != 0 and dest != 0:
            cross_cnt += 1

    return dest, cross_cnt


if __name__ == "__main__":
    print(main())
