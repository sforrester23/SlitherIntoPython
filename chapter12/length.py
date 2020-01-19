def length(argument):
    total = 0
    if type(argument) == str or type(argument) == list or type(argument) == dict:
        for item in argument:
            total += 1
        return total
    else:
        return "That is not a recognised data type."


def main():
    print(length([1,2,3]))
    print(length("This is a string"))
    print(length({"key1": 4, "key2": 3}))
    print(length({}))


if __name__ == "__main__":
    main()