''' A collection of math functions that are used multiple times throughout the euler problems'''

_primes = []
_primes_set = {}

def initialise_primes(n):
    global _primes
    global _primes_set

    ''' Initialises the collection of primes for use in the other functions 
    for performance reasons if they will be called a lot'''

    _primes = list(generate_primes(n))
    _primes_set = set(_primes)

def get_proper_divisors(n):
    ''' Finds the proper divisors of input n where
    a proper divisor is any number less than n that divides n evenly'''
    # Would definitely be nice to do some memoisation here since questions generally require
    # divisors for all numbers from 0 to n.
    
    # any numbers > n / 2 can't be proper divisors
    return [i for i in range(1, n // 2 + 1) if n % i == 0]

def generate_primes(n):
    ''' Generates primes up to n using the sieve of eratosthenes.'''
    # Taken from Rosettacode
    multiples = set()
    for i in range(2, n+1):
        if i not in multiples:
            yield i
            multiples.update(range(i*i, n+1, i))

def is_prime(n):
    '''Tests if a number n is prime'''
    if n <= 3:
        return n > 1
    elif n % 2 == 0 or n % 3 == 0:
        return False

    i = 5

    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False

        i += 6

    return True

def prime_factors(n):
    ''' Gets the prime factors of n
    Can pass in a pre generated list of primes for performance if needed'''
    if _primes == []:
        primes = list(generate_primes(n))
        primes_set = primes
    else:
        primes = _primes
        primes_set = _primes_set

    factors = []

    while n not in primes_set:
        for prime in primes:
            if n % prime == 0:
                factors.append(prime)
                n /= prime

                break
    
    factors.append(int(n))    
    return factors