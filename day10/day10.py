#!/usr/bin/env python3

import sys

matches = {"{": "}", "[": "]", "(": ")", "<": ">"}
values = {")": 3, "]": 57, "}": 1197, ">": 25137}

add_values = {")": 1, "]": 2, "}": 3, ">": 4}


def find_closing(line, current_pos, open_list=None):
    open_list = open_list or []
    if current_pos == len(line):
        return None, open_list
    cur_char = line[current_pos]
    if cur_char in matches:
        open_list.append(cur_char)
    elif cur_char == matches[open_list[-1]]:
        open_list.pop(-1)
    else:
        # wrong match
        return cur_char, []
    return find_closing(line, current_pos + 1, open_list)


if __name__ == "__main__":
    filename = sys.argv[1]
    with open(sys.argv[1]) as f:
        data = f.read().strip().splitlines()
    wrong_chars = []
    open_lists = []
    for l in data:
        c, o_l = find_closing(l, 0)
        if c:
            wrong_chars.append(c)
        if o_l:
            open_lists.append(o_l)
    total_sum = 0
    for c in wrong_chars:
        total_sum += values[c]
    print(f"{total_sum=}")

    scores = []
    for o_l in open_lists:
        line_score = 0
        for c in reversed(o_l):
            line_score *= 5
            line_score += add_values[matches[c]]
        scores.append(line_score)
    scores.sort()
    print(f"{scores[int(len(scores)/2)]=}")
