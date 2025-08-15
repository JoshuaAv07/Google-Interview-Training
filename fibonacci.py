import random

def fibonacci(n:int, memo={}):
    if n in memo:
        return memo[n]
    
    if (n <= 0):
        return 0
    elif (n == 1):
        return 1 
    
    memo[n] = fibonacci(n-1) + fibonacci(n-2)
    return memo[n]
    
if __name__ == "__main__":
    n = random.randint(0, 10)
    print(n)
    for i in range(n):
        print(fibonacci(i), end=" ")