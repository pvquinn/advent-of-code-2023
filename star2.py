import re

f = open("star1.txt", "r")
numbers = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
total = 0
for line in f:
    all_nums = re.findall("one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9", line)
    first = all_nums[0]
    if first in numbers:
        first = numbers[first]
    line = line[::-1]
    reverse_nums = re.findall("9|8|7|6|5|4|3|2|1|enin|thgie|neves|xis|evif|ruof|eerht|owt|eno", line)
    second = reverse_nums[0][::-1]
    if second in numbers:
        second = numbers[second]
    print(f'{first} {second}')
    combined = first + second
    total = total + int(combined)
print(total)
