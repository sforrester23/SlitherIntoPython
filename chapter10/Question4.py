import sys

with open(sys.argv[1], "r") as inp:
    text = inp.readline().replace(" ", "").lower().strip()

    while text:
        i = 0
        n = len(text)
        while i < n and text[i] == text[-(i+1)]:
            i += 1
        if i == n:
            print(True)
        else:
            print(False)

        text = inp.readline().replace(" ", "").lower().strip()

