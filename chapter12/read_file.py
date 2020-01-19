def read_file(file):
    with open(file, "r") as inp:
        lines = []
        line = inp.readline().strip()
        while line:
            lines.append(line)
            line = inp.readline().strip()
        return lines


def main():
    read_file("input.txt")


if __name__ == "__main__":
    main()