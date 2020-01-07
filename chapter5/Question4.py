# Higher or Lower

user_input_1 = int(input("Please enter a number: "))

while True:
    user_input_2 = int(input("Please enter another number: "))
    if user_input_2 > user_input_1:
        print("{} is higher than {}!".format(user_input_2, user_input_1))
    elif user_input_2 < user_input_1:
        print("{} is lower than {}...".format(user_input_2, user_input_1))
    else:
        print("They're the same number??")
    user_input_1 = user_input_2

