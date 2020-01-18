a = [909, 31, 42, 26, 15]

i = 1  # Assume the first element (a[0]) is sorted
while i < len(a):  # Same as with selection sort
    v = a[i]  # The value we want to insert into the correct position
    print(v)
    p = i  # The position the element should be inserted into to
    while p > 0 and v < a[p - 1]:  # While value is < element to left
        a[p] = a[p - 1]  # Move the element to left up one place
        p -= 1  # Decrement p (move one position left)
        print(a)
    a[p] = v  # Found correct position so insert the value
    print(a)

    i += 1  # Move to next element

print(a)