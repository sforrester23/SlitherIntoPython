# write a program that emulates the strip() method,
# it strips all multiple white spaces either sides of words in a string
# and replaces that string so it only has one white space in between each separate word.


s = input("Input a phrase to strip: ")

output = ""

i = 0
while i < len(s):
    while i < len(s) and s[i] == " ":
        # find a non-whitespace character
        i += 1

    j = i
    if i < len(s):
        while j < len(s) and s[j] != " ":
            # find the end of that word
            j += 1

        output += " " + s[i:j]

    i = j + 1

print(output[1:])