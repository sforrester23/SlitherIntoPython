def insert(arr, elem):
    # we work it much in the same way as binary search
    low = 0  # Define initial low value.
    high = len(arr)  # Define initial high value.

    while low != high:  # The condition that must hold true.
        mid = (low + high) // 2  # Calculate the mid index.
        if arr[mid] < elem:  # Check if the value is in first or second half.
            low = mid + 1 # Update low value if mid val < elem (in second half).
        else:
            high = mid  # Otherwise update high value (elem in first half).

    # if the placing index is within the list dimensions and the element can be placed between two numbers
    if high < len(arr) and arr[low - 1] < elem <= arr[high]:
        return "The number should be placed at position: " + str(low)
    # if the placing index is found at the end of the list, i.e. it is bigger than everything currently in there
    elif high == len(arr) and arr[low-1] < elem:
        # tell them the number should be placed at the end of the list
        return "The number should be placed at position: " + str(low)
    # if the loop ran out of time before placing it
    else:
        return "We couldn't find the correct position to place your number..."


print(insert([1, 3, 4, 6], 2))
