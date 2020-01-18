def selection_sort(a):
    # counts
    # i count point in the list where to the left it is sorted and to the right we don't know if it is sorted
    # this must be true because we are going to send the minimum of the whole list before it each loop round
    # hence designing it so that each time we add to the left of the list it is only adding the next biggest number
    i = 0
    # j is a floating index that counts through the remaining unsorted right side of the list to find the next minimum
    j = 0
    # for the duration of the list
    while i < len(a):
        # cycle each point after where the list is sorted (i.e. cycle through the unsorted section)
        # using i+j to omit the first i sorted elements
        # when the point where that minimum is found, break the loop
        # i+j, where j changes, is the point of this next lowest value
        while a[i+j] != min(a[i+j:]):
            j += 1

        # swap the list around so the next lowest value goes to the next lowest position at index i:
        # u is the value we've identified as the next lowest value
        u = a[i+j]
        # set the position where the lowest value was to what was in the position of where the lowest value is going
        a[i+j] = a[i]
        # place our next lowest value for our sorted section of the list in its ordered position
        a[i] = u
        # increment the position defining the point up to where the list is ordered
        i += 1
        # reset j so that we can use it to cycle through the remaining list again in the next loop
        j = 0
    return a


def bubble_sort(a):
    # bubble sort, attempted to do an insertion sort
    # loop through the list with i
    i = 0
    while i < len(a):
        # loop again with j, comparing pairs of adjacent values
        j = 0
        while j < len(a) - 1:
            # if the two adjacent values are in the wrong order (left is bigger than right), swap them
            if a[j] > a[j + 1]:
                u = a[j]
                a[j] = a[j + 1]
                a[j + 1] = u
            print("i:", i, "j:", j)
            print(a)
            # increment j, check the next pair of adjacent values
            j += 1
        # increment i, so we can check the whole list again and compare newly positioned adjacent values
        # this way we know we will always compare the highest value with the lowest value always
        # therefore we know they will always end up sorted in their correct positions
        i += 1
    return a


def insertion_sort(a):
    i = len(a) - 2  # Assume the last element is sorted
    while i >= 0:  # i can be at least 0 or index error
        v = a[i]  # The value we want to insert into the correct position
        print(v)
        p = i  # The position the element should be inserted into to
        while p < len(a) - 1 and v > a[p + 1]:  # While value is > element to right
            a[p] = a[p + 1]  # Move the element to right down
            p += 1  # Increment p (move one position right)
            print("inside loop:", a)
        # when loop breaks, we've found the position for our value to land
        a[p] = v  # Found correct position so insert the value
        print("outside loop", a)

        i -= 1  # Move to next element
    return a


# print(selection_sort([3, 4, 6, 1, 9]))
# print(insertion_sort([909, 3113, 420, 151, 206]))
print(bubble_sort([9, 7, 3, 8, 10, 15, 2]))