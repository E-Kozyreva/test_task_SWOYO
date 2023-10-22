import time
from math import ceil


def SieveOfEratosthenes(n: int) -> list:
    prime = [True for i in range(n + 1)] 
    p = 2
    
    while(p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    
    nums = [p for p in range(2, n) if prime[p]]
    return nums


def prime_numbers(low: int, high: int) -> list:
    if (isinstance(low, (int, float)) and 
        isinstance(high, (int, float)) and 
        low <= high):
        return [n for n in SieveOfEratosthenes(int(high)) if n >= ceil(low)]
    return []
