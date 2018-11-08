# This is a simple prime factors calculator I made when first learning Python. Uses a simple and efficient algorithm

import math

def PrimeFactors(n):
    """Return the prime factors of any number"""
    primes = []
    while n % 2 == 0:
        n = n/2
        primes.append(2)
    for i in range(3,int(math.sqrt(n)+1),2):
        while n % i == 0:
            n = n/i
            primes.append(int(i))
    if n > 1: # if its been totally factored, we wont append remainder as a prime
        primes.append(int(n))
    print(', '.join(map(str,primes)))

n = int(input('Enter the number you would like to see the Prime Factors of: '))
PrimeFactors(n)
