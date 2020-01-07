# write a formula that decides whether or not a set of three values forms a right angle triangle
import math


def right_angle_triangle(a, b, c):
    if c == max(a, b, c):
        if c == math.sqrt((a**2 + b**2)):
            print("You have a right-angled triangle!")
        else:
            print("You do not have a right_angled triangle...")
    elif b == max(a, b, c):
        if b == math.sqrt((a**2 + c**2)):
            print("You have a right-angled triangle!")
        else:
            print("You do not have a right_angled triangle...")
    elif a == max(a, b, c):
        if a == math.sqrt((b**2 + c**2)):
            print("You have a right-angled triangle!")
        else:
            print("You do not have a right_angled triangle...")


user_input_a = int(input("a = "))
user_input_b = int(input("b = "))
user_input_c = int(input("c = "))

right_angle_triangle(user_input_a, user_input_b, user_input_c)
