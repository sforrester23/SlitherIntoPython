# Fibonacci Calculator

F0 = 0
F1 = 1
index = 0
length = int(input("How many terms would you like to print? "))
fibonacci_numbers = [0, 1]

while index < length:
    F_next = F0 + F1
    fibonacci_numbers.append(F_next)
    F0 = F1
    F1 = F_next
    index += 1
print(fibonacci_numbers)