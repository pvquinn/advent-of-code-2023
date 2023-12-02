f = open("star1.txt", "r")
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
total = 0
for line in f:
    first = 10
    second = 10
    for c in line:
        if c in digits:
            second = c
            if first == 10:
                first = c
    combined = first + second
    total = total + int(combined)
print(total)
