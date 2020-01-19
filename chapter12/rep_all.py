def rep_all(a, x, y):
    if type(a) == list:
        i = 0
        while i < len(a):
            if a[i] == x:
                a[i] = y
            i += 1
    else:
        print("That first argument is not a list")


def main():
    a = [1, 3, 5, 6]
    rep_all(a, 3, 7)
    print(a)


if __name__ == "__main__":
    main()