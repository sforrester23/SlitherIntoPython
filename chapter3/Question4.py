# sequence 1
y = [0, 2, 4, 6, 8, 10, "..."]

x = 0
index = 0
while index < 5:
    print(x)
    x = x + 2
    index += 1

# sequence 2
y = [0, -1, -2, -3, -4, -5, "..."]

x = 0
index = 0
while index < 5:
    print(x)
    x = x - 1
    index += 1

# sequence 3
y = [6, -6, 6, -6, 6, "..."]

x = 6
index = 0
while index < 5:
    print(x)
    x = x * -1
    index += 1

# sequence 4
y = [0, 3, 6, "..."]

index = 1
length = 5
x = 0
while index <= length:
    x = ((x+3) % 9)
    print(x)
    index += 1

