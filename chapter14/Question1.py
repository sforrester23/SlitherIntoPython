import sys
from times_tables import times_tables_complex

flags = ["-f", "-s"]

# print(sys.argv[2] not in flags and not sys.argv[2].isnumeric())


if len(sys.argv) < 2:
    raise ValueError("You need to enter some arguments!")

elif len(sys.argv) >= 2:
    try:
        if sys.argv[1] in flags:
            raise Exception("You can't enter a flag first, put a number first...")
        number = float(sys.argv[1])
        i = 0
        count_num = 0
        while i < len(sys.argv):
            if sys.argv[i].isnumeric():
                count_num += 1
            i += 1

        if count_num != 1:
            raise Exception("You need to contain exactly ONE number in the arguments!")

        j = 2
        while j < len(sys.argv):
            if sys.argv[j] not in flags and not sys.argv[j].isnumeric():
                raise Exception("You need to only contain recognised tags! Like -f or -s.")
            j += 1

        flags_present = []
        k = 1
        while k < len(sys.argv):
            if sys.argv[k] in flags:
                if sys.argv[k] in flags_present:
                    raise Exception("You can't enter the same flag twice?")
                else:
                    flags_present.append(sys.argv[k])
            k += 1

        if flags_present == ["-f"]:
            times_tables_complex(number, "^3.0f")
        elif flags_present == ["-s"]:
            times_tables_complex(number, ".0f", short=True)
        elif flags_present == ["-f", "-s"] or flags_present == ["-s", "-f"]:
            times_tables_complex(number, ">3.0f", True)
        else:
            times_tables_complex(number, ".0f")

    except ValueError:
        print("You have to input a number as the first argument!")



