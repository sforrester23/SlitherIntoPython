import sys

with open(sys.argv[1], "r") as inp:
    line = inp.readline().strip().split()
    set_line = set(line)
    set_unique = set()

    while line:
        difference = set_line.difference(set_unique)
        print(difference)
        line = inp.readline().strip().split()
        set_line = set(line)
        set_unique = set_unique.union(difference)
        print(set_unique)

    print(len(set_unique))
