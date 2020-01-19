def add(*argv):
    total = 0
    for number in argv:
        total += number
    return total


def subtract(x, *argv):
    total = x
    for number in argv:
        total -= number
    return total


def multiply(*argv):
    total = 1
    for number in argv:
        total *= number
    return total


def divide(x, y):
    total = x//y
    return total


def main():
    print(add(3, 2, 4, 16, 77))
    print(subtract(100, 3, 4, 5))
    print(multiply(2, 3, 4, 5))
    print(divide(500, 5))


if __name__ == "__main__":
    main()