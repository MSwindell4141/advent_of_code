""" 2024 Advent of Code - Day 3: Part 2
2024-12-03 Micah Swindell
"""

import re

mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
do_pattern = r"do\(\)"
dont_pattern = r"don['’]t\(\)"
bool_do = True

sum = 0

with open('input.txt', 'r') as file:
    for line in file:
        do_indexes = [match.start() for match in re.finditer(do_pattern, line)]
        dont_indexes = [match.start() for match in re.finditer(dont_pattern, line)]
        mul_indexes = [match.start() for match in re.finditer(mul_pattern, line)]
        mul_tuples = (re.findall(mul_pattern, line))

    for i in range(len(line)):
        if i in do_indexes:
            bool_do = True
        if i in dont_indexes:
            bool_do = False
        if i in mul_indexes and bool_do:
            tuple = mul_tuples[mul_indexes.index(i)]
            sum += (int(tuple[0]) * int(tuple[1]))

print(sum)