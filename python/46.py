import lib.mathhelper as mathhelper

primes = list(mathhelper.generate_primes(10000))

for n in range(1, 9999, 2):
    if n in primes:
        continue

    found = False

    for p in primes:
        if p > n or found:
            break

        for square in range(1, n):
            res = p + 2 * square * square

            if res == n:
                found = True
                break

            if res > n:
                break

    if not found:
        print(n)