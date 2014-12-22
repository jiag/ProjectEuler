import math
i=2

n = 3
def isPrime(n):
    a = 2
    while a <= math.sqrt(n):
        if n % a ==0:
            return False
        a = a+1
    return True

while i< 10002:
    if isPrime(n):
        i=i+1
    n=n+2
print n-2, isPrime(n-2)