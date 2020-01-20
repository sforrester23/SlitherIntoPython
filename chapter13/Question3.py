def contains(arr, elem):
    # we work it much in the same way as binary search
    low = 0  # Define initial low value.
    high = len(arr)  # Define initial high value.

    while low != high:  # The condition that must hold true.
        mid = (low + high) // 2  # Calculate the mid index.
        if arr[mid] < elem:  # Check if the value is in first or second half.
            low = mid + 1 # Update low value if mid val < elem (in second half).
        else:
            high = mid  # Otherwise update high value (elem in first half).

    # if the placing index is within the list dimensions (able to index it)
    # and the index value relates to the element in the list, it is contained in the list
    if high < len(arr) and arr[high] == elem:
        return True
    else:
        return False


print(contains([1, 3, 5, 7], 3))
print(contains([1, 3, 5, 7], 7))
print(contains([1, 3, 5, 7], 2))
print(contains([1, 3, 5, 7], 12))