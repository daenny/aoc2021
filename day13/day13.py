#!/usr/bin/env python3

import sys


def fold(axis, number, points):
    new_points = set()
    if axis == "y":
        for p in points:
            if p[1] > number:
                diff = p[1] - number
                new_y = p[1] - 2 * diff
                new_points.add((p[0], new_y))
            else:
                new_points.add(p)
    if axis == "x":
        for p in points:
            if p[0] > number:
                diff = p[0] - number
                new_x = p[0] - 2 * diff
                new_points.add((new_x, p[1]))
            else:
                new_points.add(p)

    return new_points


if __name__ == "__main__":
    filename = sys.argv[1]
    with open(sys.argv[1]) as f:
        data = f.read().strip().splitlines()

    points = set()
    folds = []
    for line in data:
        if "," in line:
            a, b = line.split(",")
            points.add((int(a), int(b)))
        elif "=" in line:
            axis, num = line.split("=")
            folds.append((axis[-1], int(num)))

    for a, n in folds:
        points = fold(a, n, points)

    import matplotlib.pyplot as plt

    x = [p[0] for p in points]
    y = [-p[1] for p in points]
    plt.plot(x, y, "o", color="black")
    plt.show()
