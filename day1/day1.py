#!/usr/bin/env python3

import sys


def count_larger_than_previous(data):
    return sum([1 for z1, z2 in zip(data, data[1:]) if z2 > z1])


if __name__ == "__main__":
    filename = sys.argv[1]
    with open(sys.argv[1]) as f:
        data = f.readlines()
    filtered_data = [int(d.strip()) for d in data if d.strip()]
    larger_than_previous = count_larger_than_previous(filtered_data)
    print(f"{larger_than_previous=}")

    sliding_windows = [sum([z1, z2, z3]) for z1, z2, z3 in zip(filtered_data, filtered_data[1:], filtered_data[2:])]

    larger_than_previous_window = count_larger_than_previous(sliding_windows)
    print(f"{larger_than_previous_window=}")
