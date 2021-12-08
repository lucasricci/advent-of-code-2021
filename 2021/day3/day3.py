from collections import Counter
from AoC import AoC
import numpy as np


def parse(self):
    raw = self.read_input_txt()
    self.readings = np.array([[int(c) for c in line.strip('\n')] for line in
                              raw])


with open("input.txt") as f:
    binary = f.read().splitlines()


def part1() -> int:
    gamma, epsilon = [], []
    chunks = [[row[col] for row in binary] for col in range(12)]
    for i in range(12):
        most = Counter(chunks[i]).most_common()[0][0]
        least = Counter(chunks[i]).most_common()[1][0]
        gamma.append(most)
        epsilon.append(least)
    return int("".join(gamma), 2) * int("".join(epsilon), 2)


def part2(self) -> int:
    oxygen, carbon = np.copy(self.readings), np.copy(self.readings)
    chunk = [[row[col] for row in binary] for col in range(12)]

    for i in range(self.readings.shape[1]):
        if oxygen.shape[0] > 1:
            bit = int(np.sum(oxygen, axis=0)[i] >= oxygen.shape[0] / 2)
            oxygen = oxygen[oxygen[:, i] == bit]
        if carbon.shape[0] > 1:
            bit = int(np.sum(carbon, axis=0)[i] >= carbon.shape[0] / 2)
            carbon = carbon[carbon[:, i] == bit]

    oxygen = ''.join([str(int(g)) for g in oxygen[0]])
    carbon = ''.join([str(int(g)) for g in carbon[0]])

    return int("".join(oxygen), 2) * int("".join(carbon), 2)
