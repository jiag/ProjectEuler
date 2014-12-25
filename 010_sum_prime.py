import math

def isPrime(n):
    a = 2
    while a <= math.sqrt(n):
        if n % a ==0:
            return False
        a = a+1
    return True

i = 2
n = 3
sum = 2
while n < 2000000:
    if isPrime(n):
        sum += n
    n=n+2

print sum