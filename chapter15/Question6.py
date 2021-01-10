import sys

words = {word.strip() for word in sys.stdin}
reverse_words = [word for word in words if word[::-1] in words]

print(len(reverse_words))