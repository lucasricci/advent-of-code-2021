from collections import Counter

with open("input.txt") as f:
    binary = f.read().splitlines()


def part_one():
    gamma = []; epsilon = []
    chunks = [[row[col] for row in binary] for col in range(12)]
    for i in range(12):
        most = Counter(chunks[i]).most_common()[0][0]
        least = Counter(chunks[i]).most_common()[-1][0]
        gamma.append(most); epsilon.append(least)
    print(int("".join(gamma), 2) * int("".join(epsilon), 2))


def part_two():
    bina = [[row[col] for row in binary] for col in range(1)]
    print(bina)


if __name__ == "__main__":
    #part_one
    part_two()
