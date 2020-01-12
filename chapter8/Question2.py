words = input().split()
suffix = input()

i = 0

while i < len(words):
    if suffix in words[i]:
        print(words[i])
    i += 1

