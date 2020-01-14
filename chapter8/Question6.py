# take two lists, combine them and then order them


# collect the two lists, break collection when user inputs 0
number = int(input("Number please: "))
number_list_1 = []

while number != 0:
    number_list_1.append(number)
    number = int(input("Number please: "))

number = int(input("Number please: "))
number_list_2 = []

while number != 0:
    number_list_2.append(number)
    number = int(input("Number please: "))

# combine the two lists, which are unlikely to be sorted
number_list = number_list_1 + number_list_2

# repeating list indexer:
i = 0
# indexer for point up to where list has been checked to be in order:
j = 0

# keep doing this until j is the same length as the list
# that is, the list is all in order when j reaches the length of the list
while j < len(number_list):
    # go over the list until the point at which the minimum for the remaining unsorted list is found
    # the +j part requires that only the unsorted right hand side of the list is searched
    # we only search the remaining unsorted part of the list by using number_list[i+j:]
    # the index i+j will never exceed the list dimensions because by the time it could, the minimum will be found
    # i.e even if the minimum was at the end, it would be found and i+j would not increase any further and the loop ends
    while number_list[i+j] != min(number_list[i+j:]):
        i += 1

    # swap the numbers around by assigning a dummy variable
    # u is where the minimum that has been found is held
    u = number_list[i+j]
    # move the item in the position where the minimum will go to where the minimum was (swap them)
    number_list[i+j] = number_list[j]
    # place the minimum to the point j, below which everything in the list is already lower than this minimum
    number_list[j] = u
    # shorten the list we search for minimums in by one
    # (i.e. move one point to the right because an extra point on the left is now all sorted)
    j += 1
    # start i again so we can go back and iterate through the remaining list
    i = 0

print(number_list)
