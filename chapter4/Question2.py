# FIZZ BUZZ

user_input = int(input("What number would you like to play FIZZBUZZ with? "))

index = 1

while index <= user_input:
    if index % 5 == 0 and index % 3 == 0:
        print("{} - fizzbuzz!".format(index))
    elif index % 5 == 0:
        print("{} - buzz!".format(index))
    elif index % 3 == 0:
        print("{} - fizz!".format(index))
    else:
        print(index, "...")
    index += 1