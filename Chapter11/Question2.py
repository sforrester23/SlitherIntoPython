import sys

with open(sys.argv[1], "r") as inp:
    line = inp.readline().split()

    contacts = {}
    while line:
        contacts[line[0]] = [line[1], line[2]]
        line = inp.readline().split()

user_input = input("Please enter a name: ")
while user_input.lower().strip() != "exit":

    if user_input.capitalize() in contacts:
        print("Name: {}".format(user_input.capitalize()))
        print("Email: {}".format(contacts[user_input.capitalize()][1]))
        print("Email: {}".format(contacts[user_input.capitalize()][0]))
    else:
        print("No contact with that name.")

    user_input = input("Please enter a name: ")