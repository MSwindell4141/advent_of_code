""" 2024 Advent of Code - Day 3: Part 1
2024-12-03 Micah Swindell
"""

import re

mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
sum = 0

with open('input.txt', 'r') as file:
    for line in file:
        #print(line)
        tuples = (re.findall(mul_pattern, line))

        for tup in tuples:
            sum += (int(tup[0]) * int(tup[1]))

print(sum)
