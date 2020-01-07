# do two circles overlap?
import math

x1 = int(input("x co-ordinate circle 1 = "))
y1 = int(input("y co-ordinate circle 1 = "))
r1 = int(input("radius circle 1 = "))

x2 = int(input("x co-ordinate circle 2 = "))
y2 = int(input("y co-ordinate circle 2 = "))
r2 = int(input("radius circle 2 = "))


def distance_between_centre_two_circles(x1, x2, y1, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)


if distance_between_centre_two_circles(x1, x2, y1, y2) < r1 + r2:
    print("The circles overlap!")
elif distance_between_centre_two_circles(x1, x2, y1, y2) == r1 + r2:
    print("The circles overlap, but only just - its only an intersection in one place :O")
else:
    print("The circles do not overlap...")