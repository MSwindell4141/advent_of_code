""" 2024 Advent of Code - Day 2: Part 2
2024-12-03 Micah Swindell
"""

safe_count = 0

#Iterate through text file and split the numbers into our left and right columns.
with open('input.txt', 'r') as file:
    for line in file:
        #We assign the nums variable this way to cast each number as an integer. This breaks comparisons if it is not.
        nums = list(map(int, line.split()))

        #We try the same logic from part 1 but we try it while removing one number from the list each time. Not removing multiple numbers though.
        for x in range(len(nums)):
            curr_list = nums.copy()
            del curr_list[x]
            nums_asc = sorted(curr_list)
            nums_desc = sorted(curr_list, reverse=True)

            if curr_list == nums_asc or curr_list == nums_desc: #By storing the lists sorted asc and desc we can compare them to see if the original list is sorted.
                line_safe = True
                for x in range(len(curr_list) - 1):
                    if abs(int(curr_list[x]) - int(curr_list[x+1])) not in (1, 2, 3):
                        line_safe = False
                        break;
                if line_safe:
                    safe_count += 1
                    break;
##Tada! We have our answer.
print(safe_count)