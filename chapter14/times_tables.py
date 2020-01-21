def times_tables_formatted(number):
    i = 0
    while i <= 10:
        print("{:>3.0f} * {:>3.0f} = {:>3.0f}".format(i, number, i * number))
        i += 1


def times_tables(number):
    i = 0
    while i <= 10:
        print("{:.0f} * {:.0f} = {:.0f}".format(i, number, i*number))
        i += 1


def times_tables_short(number):
    i = 0
    while i <= 10:
        print("{:}".format(i*number))
        i += 1


def times_tables_formatted_short(number):
    i = 0
    while i <= 10:
        print("{:>3.0f}".format(i*number))
        i += 1


def times_tables_complex(number, form="", short=False):
    i = 0
    while i <= 10:
        if short:
            print("{:{}}".format(i*number, form))
        else:
            print("{:{}} * {:{}} = {:{}}".format(i, form, number, form, i*number, form))
        i += 1




def main():
    # times_tables(1)
    # times_tables(15)
    times_tables_complex(15, form="3.0f", short=True)


if __name__ == "__main__":
    main()