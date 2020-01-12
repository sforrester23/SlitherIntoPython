# 4-bit binary converter
# UPGRADE: 8-bit binary converter
import sys

user_input = input("8-bit binary number please good fellow: ")

number_total = 0
counter = 0

if len(user_input) != 8:
    print("That's not an 8-bit binary number...")
    sys.exit()

for index in user_input:
    if index != "0" and index != "1":
        print("that's not a binary number...")
        sys.exit()

while counter < 8:
    number_total += int(user_input[7 - counter]) * (2 ** counter)
    counter += 1
print(number_total)