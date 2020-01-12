my_words = input("Input some words to make a list: ").split()
num = int(input("Number please: "))

i = 0

while i < len(my_words):
    if len(my_words[i]) >= num:
        print(my_words[i])
    i += 1