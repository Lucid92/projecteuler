''' A collection of math functions that are used multiple times throughout the euler problems'''

def get_proper_divisors(n):
    ''' Finds the proper divisors of input n where
    a proper divisor is any number less than n that divides n evenly'''
    # Would definitely be nice to do some memoisation here since questions generally require
    # divisors for all numbers from 0 to n.
    
    # any numbers > n / 2 can't be proper divisors
    return [i for i in range(1, n // 2 + 1) if n % i == 0]

def generate_primes(n):
    ''' Generates primes up to n using the sieve of eratosthenes.
    Taken from Rosettacode '''
    multiples = set()
    for i in range(2, n+1):
        if i not in multiples:
            yield i
            multiples.update(range(i*i, n+1, i))

