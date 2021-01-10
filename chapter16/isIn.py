# function that determines if a character is in a given string by recursion and partitioning
def isIn(char, aStr):
    length = len(aStr)
    mid = length//2
    if length == 0:
        return False
    if char == aStr[mid]:
        return True
    elif char > aStr[mid]:
        return isIn(char, aStr[mid+1:])
    elif char < aStr[mid]:
        return isIn(char, aStr[:mid])

print(isIn("p", "abcdef"))