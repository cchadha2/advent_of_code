"""Advent of Code 2021 Day 3"""
from utils import read_input


data = read_input("day_3_input.txt")
#data = ["00100", "11110", "10110" ,"10111" ,"10101" ,"01111" ,"00111" ,"11100" ,"10000" ,"11001"
#,"00010" ,"01010"]


# Part 1
bit_length = len(data[0])
print('bit length', bit_length)
ones = [0] * bit_length

for number in data:
    for idx, integer in enumerate(number):
        if integer == "1":
            ones[idx] += 1

print(ones)
print('count of ones', ones)

N = len(data)
print('num of values', N)


gamma = [None] * bit_length
epsilon = [None] * bit_length
for idx, counts in enumerate(ones):
    num_ones, num_zeroes = counts, N - counts
    if num_ones >= num_zeroes:
        gamma[idx] = "1"
        epsilon[idx] = "0"
    else:
        gamma[idx] = "0"
        epsilon[idx] = "1"


gamma_dec, epsilon_dec = int("".join(gamma), base=2), int("".join(epsilon), base=2)
print('gamma', gamma, gamma_dec)
print('epsilon', epsilon, epsilon_dec)
print('part 1 result', gamma_dec * epsilon_dec)

# Part 2
o2 = data.copy()
co2 = data.copy()

def common(arr, position):
    ones = 0
    N = len(arr)
    for num in arr:
        if num[position] == "1":
            ones += 1

    return (1, 0) if N - ones <= ones else (0, 1)

position = bit_length - 1
while len(o2) != 1:
    most_common, _ = common(o2, bit_length - (position + 1))
    # Should be 1 if both numbers in that position are equal => XNOR.
    o2 = list(filter(lambda num: not (int(num, base=2) & 1 << position) ^ (most_common << position), o2))
    position -= 1

print('o2', o2[0], int(o2[0], base=2))

position = bit_length - 1
while len(co2) != 1:
    _, least_common = common(co2, bit_length - (position + 1))
    co2 = list(filter(lambda num: not (int(num, base=2) & 1 << position) ^ (least_common <<
        position), co2))
    position -= 1

print('co2', co2[0], int(co2[0], base=2))

print('part 2 result', int(o2[0], base=2) * int(co2[0], base=2))


