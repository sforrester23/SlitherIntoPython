import sys
import string

with open(sys.argv[1], "r") as inp:
    text_list = inp.read().lower()
    # remove all punctuation from the items in the list
    # iterate over the string
    j = 0
    while j < len(string.punctuation):
        text_list = text_list.replace(string.punctuation[j], "")
        j += 1

    # make the input into a list, now without punctuation
    text_list = text_list.split()

    i = 0
    count_unique = 0
    unique_words = []
    while i < len(text_list):
        # u is the word we're checking to see if it is unique
        u = text_list[i]

        if u not in unique_words:
            unique_words.append(u)

        i += 1

    print(unique_words)
    print(len(unique_words))
