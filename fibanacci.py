def fibonacci(n):
    fib_seq = [0, 1]
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    else:
        for i in range(2, n):
            fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq
    
print(fibonacci(5))  # Output: [0, 1, 1, 2, 3]
print(fibonacci(10)) # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
