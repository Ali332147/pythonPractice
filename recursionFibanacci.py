def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Test the function by printing the first 10 numbers in the sequence
for i in range(5):
    print(fibonacci(i))
