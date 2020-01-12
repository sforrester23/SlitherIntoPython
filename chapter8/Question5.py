number = int(input("Number please: "))
number_list = []

while number != 0:
    number_list.append(number)
    number = int(input("Number please: "))

i = 0
while number_list[i] != min(number_list):
    i += 1

u = number_list[i]
number_list[i] = number_list[0]
number_list[0] = u

print(number_list)