#!/usr/bin/env python3

import sys
import numpy as np

kernel = ([-1,0,1, -1, 1, -1, 0, 1], [-1, -1, -1, 0, 0, 1, 1, 1])

def step_board(board):
    board += 1
    idx = np.where(board > 9)
    open_list = set(zip(idx[0], idx[1]))
    visited = set()
    while open_list:
        cx, cy = open_list.pop()
        visited.add((cx,cy))
        for x,y in zip(*kernel):
            dx = cx + x
            dy = cy + y
            if dx < 0 or dy < 0 or dy >= board.shape[1] or dx >= board.shape[0]:
                continue
            board[dx, dy] += 1
            if board[dx, dy] > 9 and (dx, dy) not in visited:
                open_list.add((dx, dy))
    board[board>9] = 0
    return len(visited)
        

if __name__ == "__main__":
    filename = sys.argv[1]
    with open(sys.argv[1]) as f:
        data = f.read().strip().splitlines()
    board = []
    for line in data:
        board.append([int(x) for x in line])
    board = np.array(board)
    sum_flashed = 0
    for step in range(300):
        flashed = step_board(board)
        if flashed == board.shape[0] * board.shape[1]:
            print(f"sync on={step+1}")
            break
        sum_flashed += flashed
        if step == 99:
            print(f"{sum_flashed=}")

