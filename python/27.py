import lib.mathhelper as mathhelper

primes = set(mathhelper.primes(100000))

def consecutive_primes(a, b):
    '''Finds how many consecutive primes there are in a polynomial in the form n^2 + an + b starting at n = 0.'''

    n = 0
    while n ** 2 + n * a + b in primes:
        n += 1 

    return n

max_a = 0
max_b = 0
max_primes = 0

for a in range(-1000, 1000 + 1):
    for b in range(-1000, 1000 + 1):
        result = consecutive_primes(a, b)

        if max_primes < result:
            max_primes = result
            max_a = a
            max_b = b

print(max_primes, max_a, max_b)