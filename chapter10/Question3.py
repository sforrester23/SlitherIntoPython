import sys

with open(sys.argv[1], "r") as inp:
    words = inp.read().strip()
    words_list = words.split()

print(len(words_list))
