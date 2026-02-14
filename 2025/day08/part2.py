def main() -> int:
    input_data = parse_input()
    point_to_distance_map = build_distances_map(input_data)
    sorted_distances = build_sorted_distances(point_to_distance_map)
    p1, p2 = build_circuits(sorted_distances, len(input_data))

    return p1[0] * p2[0]


def parse_input(input_file_path: str = "input.txt") -> list[tuple[int, int, int]]:
    points = []

    with open(input_file_path, "r") as f:
        for line in f:
            line = line.strip()

            if not line:
                continue

            point = tuple(int(n) for n in line.split(","))
            points.append(point)

    return points


def build_circuits(
    distances: list[tuple[int, tuple, tuple]], total_points: int
) -> tuple[tuple, tuple]:
    point_to_circuit = {}
    counter = 0

    for distance, p1, p2 in distances:
        if p1 in point_to_circuit and p2 in point_to_circuit:
            point_to_circuit[p1].add(p1)
            point_to_circuit[p1].add(p2)
            point_to_circuit[p2].add(p1)
            point_to_circuit[p2].add(p2)
            merged_circuit = point_to_circuit[p1] | point_to_circuit[p2]
            circuit_to_index = merged_circuit
        elif p1 in point_to_circuit:
            point_to_circuit[p1].add(p1)
            point_to_circuit[p1].add(p2)
            circuit_to_index = point_to_circuit[p1]
        elif p2 in point_to_circuit:
            point_to_circuit[p2].add(p1)
            point_to_circuit[p2].add(p2)
            circuit_to_index = point_to_circuit[p2]
        else:
            new_circuit = set()
            new_circuit.add(p1)
            new_circuit.add(p2)
            point_to_circuit[p1] = new_circuit
            point_to_circuit[p2] = new_circuit
            circuit_to_index = new_circuit

        if len(circuit_to_index) == total_points:
            return p1, p2

        for point in circuit_to_index:
            point_to_circuit[point] = circuit_to_index

        counter += 1


def build_sorted_distances(distances_map: dict) -> list[tuple[int, tuple, tuple]]:
    distance_to_points = {}
    distances = set()
    result = []

    for p1 in distances_map:
        for p2 in distances_map[p1]:
            distance = distances_map[p1][p2]
            distances.add(distance)
            distance_to_points.setdefault(distance, [])
            distance_to_points[distance].append((p1, p2))

    for distance in sorted(distances):
        for p1, p2 in distance_to_points[distance]:
            result.append((distance, p1, p2))

    return result


def build_distances_map(points: list[tuple[int, int, int]]) -> dict:
    distances = {}

    for i in range(len(points)):
        for j in range(i, len(points)):
            p1 = points[i]
            p2 = points[j]
            distance = calc_distance(p1, p2)
            distances.setdefault(min(p1, p2), {})

            if distance > 0:
                distances[min(p1, p2)][max(p1, p2)] = distance

    return distances


def calc_distance(p1: tuple[int, int, int], p2: tuple[int, int, int]) -> int:
    dist = 0

    for coords in zip(p1, p2):
        dist += (coords[0] - coords[1]) ** 2

    return dist


if __name__ == "__main__":
    print(main())
