#!/usr/bin/env python3

import sys
import collections
import copy


def filter_data(input_data, default):
    res = copy.copy(input_data)

    def filter_by_common(data, index, default="1"):
        index_values = [d[index] for d in data]
        common, count = collections.Counter(index_values).most_common()[1 - int(default)]
        if count == len(index_values) / 2:
            common = default
        return [d for d in data if d[index] == common]

    for idx in range(len(input_data[0])):
        res = filter_by_common(res, idx, default)
        if len(res) == 1:
            break
    return res[0]


if __name__ == "__main__":
    filename = sys.argv[1]
    with open(sys.argv[1]) as f:
        data = f.read().strip().splitlines()
    # print(f"{data=}")
    # Part 1
    transposed = list(map(list, zip(*data)))
    # print(f"{transposed=}")
    counters = [collections.Counter(l) for l in transposed]
    gamma_counts = [counter.most_common()[0][0] for counter in counters]
    eps_counts = [counter.most_common()[1][0] for counter in counters]

    gamma = int("".join(gamma_counts), 2)
    eps = int("".join(eps_counts), 2)
    print(f"{gamma=}{eps=} multi={gamma*eps}")

    # Part 2
    oxy = int("".join(filter_data(data, "1")), 2)
    co2 = int("".join(filter_data(data, "0")), 2)

    print(f"{oxy=} {co2=} mult={oxy*co2}")
