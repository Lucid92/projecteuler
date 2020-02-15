import itertools

def solve(limit):
    perms = itertools.product(range(2, limit + 1), repeat=2)

    terms = set()
    for a, b in perms:
        terms.add(a ** b)

    return len(terms)

print(solve(100))
