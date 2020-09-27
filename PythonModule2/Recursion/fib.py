# input taken here
n = int(input())


# write code for finding nth fibonacci number
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        prev1 = fibonacci(n - 1)
        prev2 = fibonacci(n - 2)
        return prev1 + prev2


print(fibonacci(n))