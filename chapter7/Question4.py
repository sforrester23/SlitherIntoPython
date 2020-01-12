# Write a searching algorithm that will output the number of occurrences of the word

s = input("Enter a string to be searched: ")
r = input("Enter a word to search for: ")

i = 0
count = 0

while i <= len(s) - len(r):
    if s[i:i+len(r)] == r:
        count += 1
    i += 1

print(count)