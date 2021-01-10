# recursive function that takes an integer as an argument and returns whether or not that integer is a power of 2
def ispower2(n):
    if n==2:
        return True
    elif n<2:
        return False
    return ispower2(n/2)

print(ispower2((2047)))