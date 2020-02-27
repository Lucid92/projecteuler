import itertools
import math

pentagonal = set(n*(3*n -1)/2 for n in range(1, 10000))

smallest_difference = ((0,0), math.inf)
for p1, p2 in itertools.combinations(pentagonal, 2):
    D = abs(p1 - p2)
    if (p1 + p2) in pentagonal and D in pentagonal:
        if D < smallest_difference[1]:
            smallest_difference = ((p1,p2), D)

print(smallest_difference)