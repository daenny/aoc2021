#!/usr/bin/env python3

import sys
from dataclasses import dataclass


@dataclass
class SubState:
    position: int
    depth: int
    aim: int


def apply_command(command, step, current_state):
    if command == "forward":
        current_state.depth += current_state.aim * step
        current_state.position += step
    elif command == "up":
        current_state.aim -= step
    elif command == "down":
        current_state.aim += step


if __name__ == "__main__":
    filename = sys.argv[1]
    with open(sys.argv[1]) as f:
        data = f.readlines()
    commands = [(row.strip().split(" ")[0], int(row.strip().split(" ")[1])) for row in data if row.strip()]

    # part 1
    forward = sum([step for command, step in commands if command == "forward"])
    up = sum([step for command, step in commands if command == "up"])
    down = sum([step for command, step in commands if command == "down"])
    depth = down - up
    print(f"{forward=}")
    print(f"{depth=}")
    print(f"{forward*depth}")

    # part 2
    state = SubState(0, 0, 0)
    for command, step in commands:
        apply_command(command, step, state)
    print(f"{state}")
    print(f"{state.position * state.depth}")
