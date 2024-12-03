""" 2024 Advent of Code - Day 2: Part 1
2024-12-03 Micah Swindell
"""

safe_count = 0

#Iterate through text file and split the numbers into our left and right columns.
with open('input.txt', 'r') as file:
    for line in file:
        #We assign the nums variable this way to cast each number as an integer. This breaks comparisons if it is not.
        nums = list(map(int, line.split()))
        nums_asc = sorted(nums)
        nums_desc = sorted(nums, reverse=True)

        if nums == nums_asc or nums == nums_desc: #By storing the lists sorted asc and desc we can compare them to see if the original list is sorted.
            line_safe = True
            for x in range(len(nums) - 1):
                if abs(int(nums[x]) - int(nums[x+1])) not in (1, 2, 3):
                    line_safe = False
                    break;
            if line_safe:
                safe_count += 1

##Tada! We have our answer.
print(safe_count)