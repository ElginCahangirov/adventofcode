from collections.abc import Iterator
from typing import NamedTuple


class Machine(NamedTuple):
    light_diagram: list[str]
    buttons: list[tuple[int, ...]]
    joltage: list[int]


def main() -> int:
    input_data = parse_input()
    total = 0

    for machine in input_data:
        total += calc_min_button_presses(machine)

    return total


def parse_input(input_file_path: str = "input.txt") -> list[Machine]:
    machines = []

    with open(input_file_path, "r") as f:
        for line in f:
            line = line.strip()

            if not line:
                continue

            vals = line.split(" ")
            # parse light diagram
            diagram_data = vals[0]
            lights = diagram_data.strip("[]")
            light_diagram = list(lights)
            # parse buttons
            buttons_data = vals[1:-1]
            buttons = []
            for btn_data in buttons_data:
                buttons.append(tuple([int(v) for v in btn_data.strip("()").split(",")]))
            # parse joltage
            joltage_data = vals[-1]
            joltage = [int(v) for v in joltage_data.strip("{}").split(",")]

            machines.append(
                Machine(
                    light_diagram=light_diagram,
                    buttons=buttons,
                    joltage=joltage,
                )
            )

    return machines


def calc_min_button_presses(machine: Machine) -> int:
    desired_diagram = map_light_diagram_to_bits(machine.light_diagram)
    initial_diagram = [0] * len(desired_diagram)

    for n in range(1, len(desired_diagram) + 1):
        for buttons in button_combinations(machine.buttons, n):
            diagram = press_buttons(initial_diagram.copy(), buttons)
            if diagram == desired_diagram:
                return n

    raise Exception


def button_combinations(
    buttons: list[tuple[int, ...]], n: int
) -> Iterator[list[tuple[int, ...]]]:
    total = len(buttons)

    def backtrack(
        start: int, current: list[tuple[int, ...]]
    ) -> Iterator[list[tuple[int, ...]]]:
        if len(current) == n:
            yield list(current)
            return

        for i in range(start, total - (n - len(current)) + 1):
            current.append(buttons[i])
            yield from backtrack(i + 1, current)
            current.pop()

    yield from backtrack(0, [])


def map_light_diagram_to_bits(light_diagram: list[str]) -> list[int]:
    light_to_bit = {".": 0, "#": 1}
    bits = [light_to_bit[l] for l in light_diagram]
    return bits


def press_buttons(diagram: list[int], buttons: list[tuple[int, ...]]) -> list[int]:
    for button in buttons:
        for bit in button:
            diagram[bit] ^= 1

    return diagram


if __name__ == "__main__":
    print(main())
