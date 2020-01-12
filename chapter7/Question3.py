# Write a program that takes a string as input from the user.
# The string will consist of digits and your program should print out the first repdigit.
# A repdigit is a number where all digits in the number are the same.
# Examples of repdigits are 22, 77, 2222, 99999, 444444

# Building upon the previous exercise,
# write a program that takes a string as input from the user and prints the first number encountered
# along with the starting position of the number.

s = input("Please enter a string: ")
output = ""
i = 0

while i < len(s) - 1 and not (s[i].isnumeric() and s[i] == s[i+1]):
    i += 1

j = i

if i >= len(s) - 1 or s[i] != s[i+1]:
    print("There is no repdigit in that string.")
else:
    while j < len(s) - 1 and s[j].isnumeric() and s[j+1] == s[j]:
        output += s[j]
        j += 1
    output += s[j]
    print("The first number in that string is: {}, starting at position: {}".format(output, i))




