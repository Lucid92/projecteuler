import lib.mathhelper as mathhelper

mathhelper.initialise_primes(1000000)

four_factors = []

for n in range(3, 1000000):
    factors = mathhelper.prime_factors(n)
    if len(set(factors)) == 4:
        four_factors.append(n)

        if len(four_factors) == 4:
            print(four_factors)

            break
    else:
        if len(four_factors) != 0:
            four_factors.clear()
