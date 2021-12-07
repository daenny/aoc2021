#!/usr/bin/env python3

import sys
import numpy as np


if __name__ == "__main__":
    filename = sys.argv[1]
    with open(sys.argv[1]) as f:
        data = f.read().strip().splitlines()
    start_row = np.array([int(x) for x in data[0].split(",")])
    max_num = np.max(start_row)
    num_crab_per_nr = np.zeros(max_num + 1)
    for x in start_row:
        num_crab_per_nr[x] += 1
    # distance = list(range(len(num_crab_per_nr)))
    distance = [0]
    for i in range(1, len(num_crab_per_nr)):
        distance.append(distance[i - 1] + i)
    neg_distance = list(reversed(distance))
    neg_distance.pop()
    distances = np.array(neg_distance + distance)
    sums = []
    for idx in range(len(num_crab_per_nr)):
        distances_nr = distances[max_num - idx : len(distances) - idx]
        print(distances_nr)
        multi = distances_nr * num_crab_per_nr
        sums.append(np.sum(multi))
    print(min(sums))
