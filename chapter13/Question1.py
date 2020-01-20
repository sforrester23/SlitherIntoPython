# This is a supplement to question 1 answers

from random import randint


def binary_search(arr, elem):
    low = 0  # Define initial low value.
    high = len(arr)  # Define initial high value.
    i = 0
    n = 20
    while low < high and i < n:  # The condition that must hold true.
        mid = (low + high) // 2  # Calculate the mid index.
        print(i)
        print("mid", mid)
        print("low:", low, "high:", high)
        print("difference:", high - low)
        print(arr[low:high+1])
        print(arr[mid] < elem)
        if arr[mid] < elem:  # Check if the value is in first or second half.
            low = mid + 1 # Update low value if mid val < elem (in second half).
        else:
            high = mid  # Otherwise update high value (elem in first half).
        i += 1
    if i < n:
        return "The secret number is " + str(low)
    else:
        return "Sorry, we didn't find the number"


arr = [0, 1, 2, 3, 4, 6, 7, 8, 9]
elem = 5

print(elem)
print(binary_search(arr, elem))