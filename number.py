def isPrime(n):
    for i in range(2, n//2 + 1):
        if n % i == 0:
            return False
    return True

def isEven(n):
    return n % 2 == 0

def isOdd(n):
    return n % 2 == 1
