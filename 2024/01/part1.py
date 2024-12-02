""" 2024 Advent of Code - Day 1: Part 1
2024-12-02 Micah Swindell
"""

sum = 0
left_col = []
right_col = []

#Iterate through text file and split the numbers into our left and right columns.
with open('input.txt', 'r') as file:
    for line in file:
        nums = line.split()
        left_col.append(int(nums[0]))
        right_col.append(int(nums[1]))

#This sort function automatically sorts them in ascending order. Gotta love python
left_col.sort()
right_col.sort()

#Iterate through the columns and add the absolute difference between the two columns to our sum.
for x in range(len(left_col)):
    sum += abs(left_col[x] - right_col[x])

##Tada! We have our answer.
print(sum)