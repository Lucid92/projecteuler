import lib.mathhelper as mathhelper
import itertools

# generating a prime set will be quicker than checking every time.
primes = set(mathhelper.generate_primes(10000))

res = []

for n in range(1000, 10000):
    if n in primes:
        perms = [int(''.join(i)) for i in itertools.permutations(str(n), 4)]
        # filter those that started with 0 and arent prime
        perms = [i for i in perms if i > 1000 and i in primes]

        # get all groups of 3 then check if the different between the 3 is the same when sorted
        for group in itertools.combinations(perms, 3):
            sorted_group = sorted(group)

            if sorted_group[0] - sorted_group[1] == sorted_group[1] - sorted_group[2] and sorted_group[0] - sorted_group[1] != 0:
                res.append(sorted_group)

print(res)