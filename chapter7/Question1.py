# Write a program that takes a string from the user and prints the first number encountered along with its position.

s = input("Please enter a string: ")
output = ""
i = 0

while i < len(s) and not s[i].isnumeric():
    i += 1
if i < len(s):
    output += s[i]
    print("The first number in the string is: {}, at position: {}".format(output, i))
else:
    print("There is no number in that string.")

