r = int(input("Radius: "))
i = int(input("Increment: "))
end = int(input("End Increment: "))
pi = 3.14159


def area_sphere(r):
    return 4*pi*(r**2)


def volume_sphere(r):
    return (4/3)*pi*(r**3)


counter = 0

print("{:>10}".format("Radius"), " ", "{:>10}".format("Area"), " ", "{:>10}".format("Volume"))
print("{:>10}".format("-"*10), " ", "{:>10}".format("-"*10), " ", "{:>10}".format("-"*10))

while r <= end:
    area = area_sphere(r)
    volume = volume_sphere(r)
    print("{:>10.2f}".format(r), " ", "{:>10.2f}".format(area), " ", "{:>10.2f}".format(volume))
    r += i

    counter += 1