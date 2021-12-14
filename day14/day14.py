#!/usr/bin/env python3

import sys
import collections


def do_inserts(input_p, pair_inserts):
    new_pairs = collections.defaultdict(int)
    for pair, count in input_p.items():
        new_pairs[pair_inserts[pair][0]] += count
        new_pairs[pair_inserts[pair][1]] += count

    return new_pairs


if __name__ == "__main__":
    filename = sys.argv[1]
    with open(sys.argv[1]) as f:
        data = f.read().strip().splitlines()

    input_pol = data[0]
    input_pairs = collections.defaultdict(int)
    for x, y in zip(input_pol, input_pol[1:]):
        input_pairs[x, y] += 1

    pair_inserts = {}
    for line in data[2:]:
        (x, y), target = line.split(" -> ")
        pair_inserts[(x, y)] = [(x, target), (target, y)]

    for _ in range(40):
        input_pairs = do_inserts(input_pairs, pair_inserts)

    counts = collections.defaultdict(int)
    for (x, y), count in input_pairs.items():
        counts[x] += count
        counts[y] += count

    # everything is counted double, except first and last letter
    counts[input_pol[0]] += 1
    counts[input_pol[-1]] += 1

    min_value = min(v for v in counts.values())
    max_value = max(v for v in counts.values())
    result = (max_value - min_value) / 2
    print(f"{result=}")
