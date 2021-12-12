"""Advent of Code 2021 Day 1"""
from utils import read_input

data = read_input("day_1_input.txt")

increased = 0
data[0] = int(data[0])

# Linear scan.
for idx in range(1, len(data)):
    data[idx] = int(data[idx])
    if data[idx] - data[idx - 1] > 0:
        increased += 1

print(increased)

# Sliding window.
start, end = 0, 2
curr = sum(data[idx] for idx in range(end + 1))
increased = 0
while end < len(data) - 1:
    end += 1
    next_sum = curr - data[start] + data[end]

    if next_sum > curr:
        increased += 1

    curr = next_sum
    start += 1

print(increased)

