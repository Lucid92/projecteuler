import lib.mathhelper as mathhelper

def get_all_rotations(n):
    rotations = [n]
    for _ in range(len(str(n)) - 1):
        rotations.append(rotate(rotations[-1]))

    return rotations

def rotate(n):
    ''' Rotates a number to the left one position'''
    n_str = str(n)
    return int(n_str[1:] + n_str[0])

primes = set(mathhelper.generate_primes(1000000))

results = []

for prime in primes:
    # Ignore primes with zeros since the rotation will cause an invalid number according to the question.
    if '0' in str(prime):
        continue

    if all(i in primes for i in get_all_rotations(prime)):
        results.append(prime)

print(len(results))