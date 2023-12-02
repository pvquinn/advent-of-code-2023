import re

f = open("star3.txt", "r")
total = 0
for line in f:
    product = 1
    for color in ['red', 'blue', 'green']:
        pattern = f'\d*(?= {color})'
        all_nums = re.findall(pattern, line)
        clean = False
        while clean is False:
            if '' in all_nums:
                all_nums.remove('')
            else:
                clean = True
        for i in range(0, len(all_nums)):
            all_nums[i] = int(all_nums[i])
        maximum = max(all_nums)
        product = product * maximum
    total += product
print(total)

