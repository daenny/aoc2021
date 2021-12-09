#!/usr/bin/env python3

import sys
import numpy as np

kernel = list(zip([1, 0, -1, 0], [0, 1, 0, -1]))


def find_basin_size(idx, board):
    open_list = set([idx])
    visited = set()
    while open_list:
        new = open_list.pop()
        visited.add(new)
        for kx, ky in kernel:
            new_p = (new[0] + kx, new[1] + ky)
            if new_p in visited:
                continue
            if board_with_boarder[new_p] < 9:
                open_list.add(new_p)
    return len(visited)


if __name__ == "__main__":
    filename = sys.argv[1]
    with open(sys.argv[1]) as f:
        data = f.read().strip().splitlines()
    board = [[int(x) for x in line] for line in data]
    board_with_boarder = [[10] * (len(board[0]) + 2)]
    for line in board:
        board_with_boarder.append([10] + line + [10])
    board_with_boarder.append([10] * (len(board[0]) + 2))
    board_with_boarder = np.array(board_with_boarder)
    total_sum = 0
    min_points = []
    for row in range(1, board_with_boarder.shape[0] - 1):
        for column in range(1, board_with_boarder.shape[1] - 1):
            min_nr = board_with_boarder[row, column]
            for kx, ky in kernel:
                if min_nr >= board_with_boarder[row + kx, column + ky]:
                    break
            else:
                min_points.append((row, column))
                total_sum += min_nr + 1
    print(total_sum)
    basin_sizes = []
    for min_p in min_points:
        basin_sizes.append(find_basin_size(min_p, board_with_boarder))
    basin_sizes.sort()
    print(basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3])
