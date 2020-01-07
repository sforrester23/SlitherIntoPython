# stars display 

number_of_stars = int(input("How many stars would you like? "))

index = 0

while index < number_of_stars:
    index+=1
    print(index*"*")


while index > 1:
    index-=1
    print(index*"*")
