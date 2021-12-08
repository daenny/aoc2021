#!/usr/bin/env python3

import sys
import enum
import numpy as np
from collections import defaultdict


class Segments(enum.Enum):
    TOP = 1
    CENTER = 2
    BOTTOM = 3
    TL = 4
    TR = 5
    BL = 6
    BR = 7


def deduce_segments(input_values):
    segments = {}
    numbers = []
    for _ in range(10):
        numbers.append([])
    for x in input_values:
        if len(x) == 2:
            numbers[1].append(set(x))
        if len(x) == 3:
            numbers[7].append(set(x))
        if len(x) == 4:
            numbers[4].append(set(x))
        if len(x) == 5:
            numbers[2].append(set(x))
            numbers[3].append(set(x))
            numbers[5].append(set(x))
        if len(x) == 6:
            numbers[6].append(set(x))
            numbers[0].append(set(x))
            numbers[9].append(set(x))
        if len(x) == 7:
            numbers[8].append(set(x))

    segments[Segments.TOP] = numbers[7][0] - numbers[1][0]

    search_set = numbers[4][0] | segments[Segments.TOP]

    for option in numbers[9]:
        if len(option & search_set) == 5:
            nine = option
    numbers[9] = [nine]
    segments[Segments.BOTTOM] = numbers[9][0] - numbers[4][0] - segments[Segments.TOP]
    segments[Segments.BL] = numbers[8][0] - numbers[9][0]

    search_set = numbers[7][0] | segments[Segments.BOTTOM]
    for option in numbers[3]:
        if len(option - search_set) == 1:
            three = option
    numbers[3] = [three]
    segments[Segments.CENTER] = numbers[3][0] - search_set

    numbers[0] = [numbers[8][0] - segments[Segments.CENTER]]
    for option in numbers[6]:
        if option != numbers[0][0] and option != numbers[9][0]:
            six = option
    numbers[6] = [six]

    segments[Segments.TR] = numbers[8][0] - numbers[6][0]
    segments[Segments.BR] = numbers[1][0] - segments[Segments.TR]
    numbers[2] = [(numbers[3][0] - segments[Segments.BR]) | segments[Segments.BL]]
    numbers[5] = [numbers[6][0] - segments[Segments.BL]]
    return [n[0] for n in numbers]


if __name__ == "__main__":
    filename = sys.argv[1]
    with open(sys.argv[1]) as f:
        data = f.read().strip().splitlines()
    split = [line.split("|") for line in data]
    output = [line[1].split() for line in split]
    input_values = [line[0].split() for line in split]
    total_sum = 0
    for inp, out in zip(input_values, output):
        res = deduce_segments(inp)
        num = ""
        for v in out:
            num += str(res.index(set(v)))

        total_sum += int(num)

    print(total_sum)
