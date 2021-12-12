"""Common utilities for Advent of Code stuff."""


def read_input(path):
    with open(path, "rt") as f:
        return [row.rstrip() for row in f.readlines()]

