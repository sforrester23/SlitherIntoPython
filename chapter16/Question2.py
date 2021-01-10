# recursive function that sums all numbers up to value n 
# e.g n = 100, the function outputs the sum of 100+99+98+97+...etc
def sum(n):
    if n == 1:
        return 1
    return sum(n-1)+n

print(sum(100))
    