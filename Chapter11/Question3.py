import sys
import string

with open(sys.argv[1], "r") as inp:
    word_list = inp.read().split()

    for index in range(0, len(word_list)):
        word_list[index] = word_list[index].strip(string.punctuation)

    word_dictionary = {}
    i = 0
    while i < len(word_list):
        if word_list[i].lower() not in word_dictionary:
            word_dictionary[word_list[i].lower()] = 1
        elif word_list[i].lower() in word_dictionary:
            word_dictionary[word_list[i].lower()] += 1
        i += 1

    print(word_dictionary) # There should exist 58 "the" instance (contrary to question stipulation)
