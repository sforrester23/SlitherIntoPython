import sys

file_list = sys.stdin.read().split()
vowel_set = {"a", "e", "i", "o", "u"}

list_words_vowels = [x for x in file_list if set(x).issuperset(vowel_set)]

print(len(list_words_vowels))
print("equation" in list_words_vowels)
