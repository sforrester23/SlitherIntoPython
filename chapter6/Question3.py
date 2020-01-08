import pydoc
# password = input("Password: ")
password = input("Password: ")
# print(password.lower())
# print(password.isalnum())
# print("h"=="H")
lower_alphabet="abcdefghijklmnopqrstuvwxyz"
upper_alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
characters = "!£$%&*"
numbers = "1234567890"


def contains_lower_case(password):
    for letter in lower_alphabet:
        for character in password:
            if character == letter:
                return True


def contains_upper_case(password):
    for letter in upper_alphabet:
        for character in password:
            if character == letter:
                return True


def contains_number(password):
    for number in numbers:
        for character in password:
            if character == number:
                return True


def contains_character(password):
    for special_character in characters:
        for character in password:
            if character == special_character:
                return True


def password_strength_value(password):
    password_strength = 0
    if len(password) > 0:
        if contains_lower_case(password):
            password_strength += 1
        if contains_upper_case(password):
            password_strength += 1
        if contains_number(password):
            password_strength += 1
        if contains_character(password):
            password_strength += 1
    return password_strength


print(password_strength_value(password))


