""" 2024 Advent of Code - Day 1: Part 2
2024-12-02 Micah Swindell
"""

similarity_score = 0
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

for num in left_col:
    instace_count = 0 #This keeps track of how many times we find num in right_col. It will be multiplied with num at the end for the running similarity score
    for num2 in right_col:
        if num == num2:
            instace_count += 1
    similarity_score += num * instace_count

##Tada! We have our answer.
print(similarity_score)