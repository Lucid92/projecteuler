# Solution will be to sum a consecutive window of primes and check if it's equal to a prime. 
import lib.mathhelper as mathhelper

limit = 1000000

primes = list(mathhelper.generate_primes(limit))
prime_set = set(primes)

# Find the largest possible window size before starting.
window_size = 0
s = 0
for i, p in enumerate(primes):
    s += i
    if s > limit:
        window_size = i
        break

offset = 0

while window_size > 1:    
    candidate = sum(primes[offset:offset + window_size])
    
    if candidate in prime_set:
        print(candidate)
        break

    offset += 1
    if offset + window_size > len(primes) or candidate > primes[-1]:
        window_size -= 1
        offset = 0