# the fibonacci sequence is a sequence of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1. The sequence goes: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...



def fibonacci(n):
    a, b = 0, 1
    result = []
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result

print(fibonacci(20))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
