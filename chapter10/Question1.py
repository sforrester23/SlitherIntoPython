# write a file that takes in arbitrary numbers and multiplies them together
# takes in arguments in the console and outputs there

import sys

# start index at 1 so you don't hit the first component, which is the file name
i = 1
output = 1

while i < len(sys.argv):
    output = output * int(sys.argv[i])
    i += 1

print(output)