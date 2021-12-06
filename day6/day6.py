#!/usr/bin/env python3

import sys
import numpy as np


if __name__ == "__main__":
    filename = sys.argv[1]
    with open(sys.argv[1]) as f:
        data = f.read().strip().splitlines()
    start_row = np.array([int(x) for x in data[0].split(",")])
    num_fish_per_nr = np.zeros(9)
    for x in start_row:
        num_fish_per_nr[x] += 1

    for _ in range(256):
        zeros = num_fish_per_nr[0]
        num_fish_per_nr = num_fish_per_nr[1:]
        num_fish_per_nr = np.append(num_fish_per_nr, [0])
        num_fish_per_nr[8] = zeros
        num_fish_per_nr[6] += zeros

    print(sum(num_fish_per_nr))
