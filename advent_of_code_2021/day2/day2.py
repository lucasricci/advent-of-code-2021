with open("input.txt") as f:
    lines = f.read().splitlines()


def part_one():

    horizontal = 0
    depth = 0

    for i, v in enumerate(lines):
        if v[0] == 'f':
            horizontal = horizontal + int(v[-1])
        elif v[0] == 'd':
            depth = depth + int(v[-1])
        elif v[0] == 'u':
            depth = depth - int(v[-1])

    print(f"Day 2 - Part One: {horizontal * depth}")


def part_two():

    aim = 0
    horizontal = 0
    depth = 0

    for i, v in enumerate(lines):
        if v[0] == 'f':
            horizontal += int(v[-1])

            if aim != 0:
                depth = depth + (int(v[-1]) * aim)

        elif v[0] == 'd':
            aim = aim + int(v[-1])

        elif v[0] == 'u':
            aim = aim - int(v[-1])

    print(f"Day 2 - Part Two: {horizontal * depth}")


if __name__ == "__main__":
    part_one()
    part_two()
