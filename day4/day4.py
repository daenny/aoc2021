#!/usr/bin/env python3

import sys
import dataclasses


@dataclasses.dataclass
class CheckedNumber:
    number: int
    checked: bool


def mark_board(board, number):
    for row in board:
        for checked_number in row:
            if checked_number.number == number:
                checked_number.checked = True
                return


def check_board(board):
    def check_row(row):
        if all(checked_number.checked for checked_number in row):
            return True
        return False

    transposed = list(map(list, zip(*board)))
    return any(check_row(r) for r in board) or any(check_row(r) for r in transposed)


def sum_unmarked(board):
    sum = 0
    for row in board:
        for checked_number in row:
            if not checked_number.checked:
                sum += checked_number.number
    return sum


def parse_boards(input_lines, board_size=5):
    boards = []
    line = input_lines.pop(0)
    while input_lines:
        while not len(line) > 1:
            line = input_lines.pop(0)
        board = []
        for _ in range(board_size):
            board.append([CheckedNumber(int(nr), False) for nr in line.strip().split(" ") if nr])
            if not input_lines:
                break
            line = input_lines.pop(0)
        boards.append(board)
    return boards


if __name__ == "__main__":
    filename = sys.argv[1]
    with open(sys.argv[1]) as f:
        data = f.read().strip().splitlines()
    input_numbers = [int(nr) for nr in data[0].split(",")]
    boards = parse_boards(data[1:])

    for nr in input_numbers:
        to_del = []
        for idx, b in enumerate(boards):
            mark_board(b, nr)
            if check_board(b):
                if len(boards) == 1:
                    sum_unchecked = sum_unmarked(b)
                    print(f"{nr=}{sum_unchecked=} multi={nr*sum_unchecked}")
                to_del.append(idx)
        for idx in reversed(to_del):
            boards.pop(idx)
