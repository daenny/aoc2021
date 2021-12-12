#!/usr/bin/env python3

import sys
import copy
from collections import defaultdict

neighbours = defaultdict(set)


def search_paths(neighbours, allow_double=False):
    paths = set([tuple(["start"])])

    finished_paths = set()
    while paths:
        path = paths.pop()
        for n in neighbours[path[-1]]:
            if n == "end":
                finished_paths.add(path)
            elif n == "start":
                continue
            elif n.isupper() or n not in path:
                p = list(path)
                p.append(n)
                paths.add(tuple(p))
            elif allow_double and n.islower() and not path[0] == "double":
                p = list(path)
                p.append(n)
                p.insert(0, "double")
                paths.add(tuple(p))

    return finished_paths


if __name__ == "__main__":
    filename = sys.argv[1]
    with open(sys.argv[1]) as f:
        data = f.read().strip().splitlines()
    for line in data:
        a, b = line.split("-")
        neighbours[a].add(b)
        neighbours[b].add(a)
    paths = search_paths(neighbours, False)
    print(len(paths))

    paths = search_paths(neighbours, True)
    print(len(paths))
