import re

f = open("star3.txt", "r")
counter = 0
total = 0
for line in f:
    counter += 1
    game = re.search("15 |16 |17 |18 |19 |20 |13 red|14 red|14 green", line)
    if not game:
        total += counter
print(total)
