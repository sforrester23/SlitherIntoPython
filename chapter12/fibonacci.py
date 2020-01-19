def fib(n):
    n_previous1 = 1
    n_previous2 = 1
    if n == 0:
        return n_previous1
    elif n == 1:
        return n_previous2
    elif n > 1:
        i = 2
        while i <= n:
            n_next = n_previous1 + n_previous2
            n_previous1 = n_previous2
            n_previous2 = n_next
            i += 1
        return n_next


def main():
    print(fib(13))


if __name__ == "__main__":
    main()