from math import *

largest_pri = 1
n = 600851475143
factor = 3

def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

while factor <= n:
    if isPrime(factor):
        if n%factor ==0:
            largest_pri = factor;
            n = n/factor;
    factor = factor + 2

print largest_pri