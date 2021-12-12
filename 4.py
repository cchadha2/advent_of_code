"""Advent of Code 2021 Day 4"""
import sys

from utils import read_input


data = read_input("4.txt")

numbers = list(map(int, data[0].split(",")))

boards = []
reverse_idx = []
N = 5
idx = 2
while idx < len(data):

    curr_board = []
    reverse = {}

    # Tracker for numbers left in columns.
    curr_board.append([N] * (N + 1))

    row = 1
    total = 0
    while idx < len(data) and data[idx] != "":
        # Add current row to board, prefixed with number of numbers left in row.
        curr_board.append([N] + list(map(int, data[idx].split())))
        for col, value in enumerate(curr_board[-1][1:], start=1):
            total += value
            reverse.setdefault(value, []).append((row, col))

        row += 1
        idx += 1

    boards.append(curr_board)

    reverse["total"] = total
    reverse_idx.append(reverse)

    idx += 1


def check_winner(num, board, idxs):
    if not num in idxs:
        return

    # Find the total sum of the numbers in the board.
    idxs["total"] -= len(idxs[num]) * num

    for row, col in idxs[num]:
        # Decrement the row and column count for those idxs.
        board[row][0] -= 1
        # If either are 0, we've found a winner!
        if not board[row][0]:
            return idxs["total"] * num

        board[0][col] -= 1
        if not board[0][col]:
            return idxs["total"] * num

    del idxs[num]


for num in numbers:
    for idx in range(len(boards)):
        if not boards[idx]:
            continue

        res = check_winner(num, boards[idx], reverse_idx[idx])
        if res is not None:
            boards[idx] = None
            print("winner", idx + 1, "total", res)

