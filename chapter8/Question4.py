number = int(input("Number please: "))
number_list = []

while number != 0:
    number_list.append(number)
    number = int(input("Number please: "))

print(number_list)

i1 = int(input("Please enter an integer: "))
i2 = int(input("Please enter another integer: "))

u = number_list[i1]
number_list[i1] = number_list[i2]
number_list[i2] = u

print(number_list)