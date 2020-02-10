import itertools

print(sorted(str(i) for i in itertools.permutations(range(10), 10))[1000000 - 1])