from collections import Counter
from random import choice

with open("input.txt") as f:
    binary = f.read().splitlines()


def part_one() -> int:
    gamma, epsilon = [], []
    chunks = [[row[col] for row in binary] for col in range(12)]
    for i in range(12):
        most = Counter(chunks[i]).most_common()[0][0]
        least = Counter(chunks[i]).most_common()[-1][0]
        gamma.append(most); epsilon.append(least)
    return int("".join(gamma), 2) * int("".join(epsilon), 2)


def part_two():
    oxygen_rate, carbon_rate, common = [], [], []
    oxygen = [[row[col] for row in binary] for col in range(12)]
    carbon = [[row[col] for row in binary] for col in range(12)]

    for i in range(12):
        most = Counter(oxygen[i]).most_common()[0][0]
        common.append(most)

    for n in range(12):
        if binary[0][n] != common[n]:
            binary.remove(binary[n])
    print(binary)


if __name__ == "__main__":
    print(part_one())
    part_two()
