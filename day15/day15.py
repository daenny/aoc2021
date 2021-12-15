#!/usr/bin/env python3

import sys
import numpy as np
import astar

# shamelessly copied and adjusted from https://github.com/jrialland/python-astar/blob/master/tests/maze/test_maze.py
class MazeSolver(astar.AStar):
    def __init__(self, board):
        self.board = board
        self.width = self.board.shape[0]
        self.height = self.board.shape[1]

    def heuristic_cost_estimate(self, n1, n2):
        """computes the 'manhattan' distance between two (x,y) tuples"""
        (x1, y1) = n1
        (x2, y2) = n2
        return (abs(x2 - x1) + abs(y2 - y1)) / 2

    def distance_between(self, n1, n2):
        """Costs are given by the board by entering the second node"""
        (x2, y2) = n2
        return board[x2][y2]

    def neighbors(self, node):
        """ for a given coordinate in the maze, returns up to 4 adjacent(north,east,south,west)
            nodes that can be reached (=any adjacent coordinate that is not a wall)
        """
        x, y = node
        return [
            (nx, ny)
            for nx, ny in [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]
            if 0 <= nx < self.width and 0 <= ny < self.height
        ]


if __name__ == "__main__":
    filename = sys.argv[1]
    with open(sys.argv[1]) as f:
        data = f.read().strip().splitlines()
    for tiles in [1, 5]:
        board = []
        for t_y in range(tiles):
            for line in data:
                target_line = []
                for t_x in range(tiles):
                    target_line.extend([int(x) + t_y + t_x for x in line])
                board.append(target_line)
        board = np.array(board)
        board[board > 9] -= 9

        start = (0, 0)
        end = (len(board[0]) - 1, len(board) - 1)

        path = list(MazeSolver(board).astar(start, end))

        costs = sum([board[x][y] for x, y in path[1:]])
        print(f"{tiles=} {costs=}")
