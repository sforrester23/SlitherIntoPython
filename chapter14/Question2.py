def binary_search(arr, elem):
    low = 0  # Define initial low value.
    high = len(arr)  # Define initial high value.

    while low < high:  # The condition that must hold true.
        mid = (low + high) // 2  # Calculate the mid index.

        if arr[mid] < elem:  # Check if the value is in first or second half.
            low = mid + 1 # Update low value if mid val < elem (in second half).
        else:
            high = mid  # Otherwise update high value (elem in first half).
        try:
            assert(low != mid)
        except AssertionError:
            print("low became equal to mid! This is not allowed.")
            break

    return low  # Return the position of the element we're searching for.


print(binary_search([x for x in range(0,100)], 56))

