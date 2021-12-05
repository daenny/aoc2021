#!/usr/bin/env python3

import sys
import numpy as np


def mark_line(board, line):
    diff = line[1] - line[0]
    if diff[1] == 0:
        row = line[0, 1]
        marker = np.zeros(board.shape[0])
        if diff[0] > 0:
            marker[line[0, 0] : line[1, 0] + 1] = 1
        else:
            marker[line[1, 0] : line[0, 0] + 1] = 1
        board[row, :] += marker
    if diff[0] == 0:
        column = line[0, 0]
        marker = np.zeros(board.shape[0])
        if diff[1] > 0:
            marker[line[0, 1] : line[1, 1] + 1] = 1
        else:
            marker[line[1, 1] : line[0, 1] + 1] = 1
        board[:, column] += marker
    if abs(diff[0]) == abs(diff[1]):
        for p in range(abs(diff[0]) + 1):

            p_new = line[0] + p * np.array([np.sign(diff[0]), np.sign(diff[1])])
            board[p_new[1], p_new[0]] += 1


if __name__ == "__main__":
    filename = sys.argv[1]
    with open(sys.argv[1]) as f:
        data = f.read().strip().splitlines()
    lines = []
    for line in data:
        left, right = line.split(" -> ")
        x1, y1 = left.split(",")
        x2, y2 = right.split(",")
        lines.append([[int(x1), int(y1)], [int(x2), int(y2)]])
    input_lines = np.array(lines)
    max_nr = np.max(input_lines)
    board = np.zeros((max_nr + 1, max_nr + 1))
    for line in input_lines:
        mark_line(board, line)
    print(np.sum(board > 1))
