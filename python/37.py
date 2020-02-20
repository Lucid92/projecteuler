import lib.mathhelper as mathhelper
from enum import Enum

class Direction(Enum):
    Left = 0,
    Right = 1

primes = set(mathhelper.primes(1000000))

def is_truncatable_prime(n, direction : Direction):
    if n not in primes:
        return False
    str_n = str(n)

    if len(str_n) == 1:
        return n in primes
    
    trunc = str_n[1:] if direction == Direction.Left else str_n[:-1]
    return is_truncatable_prime(int(trunc), direction)
    
results = []

for prime in primes:
    if is_truncatable_prime(prime, Direction.Left) and is_truncatable_prime(prime, Direction.Right):
        results.append(prime)

print(results)
print(sum(results) - 17) # - 17 to remove 2 through 7