def part_one():
    with open("puzzleinput.txt") as f:
        lines = f.read().splitlines()

    increase = 0
    last_number = None

    for line in lines:
        if last_number is not None:
            if int(line) > last_number:
                increase += 1
        last_number = int(line)

    print(f"Day 1 - Part One: {increase}")


def part_two():
    with open("puzzleinput.txt") as f:
        lines = f.read().splitlines()

    increase = 0

    for i in range(1, len(lines) - 3):
        a = int(lines[i]) + int(lines[i+1]) + int(lines[i+2])
        b = int(lines[i+1]) + int(lines[i+2]) + int(lines[i+3])
        if b > a:
            increase += 1

    print(f"Day 1 - Part Two: {increase}")


if __name__ == "__main__":
    part_one()
    part_two()
