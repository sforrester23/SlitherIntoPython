import sys


file = sys.stdin.read().split()

words_over_length = [x for x in file if len(x) > 18]

print(len(words_over_length))