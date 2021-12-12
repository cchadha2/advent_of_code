"""Advent of Code 2021 Day 2"""
from utils import read_input


data = read_input("day_2_input.txt")

# Part 1.
position = depth = 0
for instruction in data:
    direction, increment = instruction.split()
    increment = int(increment)

    if direction == "forward":
        position += increment
        continue

    depth += increment if direction == "down" else -increment

print(position * depth)


# Part 2.
position = depth = aim = 0
for instruction in data:
    direction, increment = instruction.split()
    increment = int(increment)

    if direction == "forward":
        position += increment
        depth += aim * increment
        continue

    aim += increment if direction == "down" else -increment


print(position * depth)


