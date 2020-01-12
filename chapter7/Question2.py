# Building upon the previous exercise,
# write a program that takes a string as input from the user and prints the first number encountered
# along with the starting position of the number.

s = input("Please enter a string: ")
output = ""
i = 0

while i < len(s) and not s[i].isnumeric():
    i += 1

j = i

if i >= len(s):
    print("There is no number in that string.")
else:
    while j < len(s) and s[j].isnumeric():
        output += s[j]
        j += 1
    print("The first number in that string is: {}, starting at position: {}".format(output, i))




