import math

def solve_quadratic(a, b, c):
    v1 = (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
    v2 = (-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)

    return (v1, v2)

def is_pentagonal_number(n):
    # P = n(3n-1)/2
    # 3n^2 - n - 2P = 0
    v1, _ = solve_quadratic(3, -1, -2 * n)

    return v1.is_integer() and v1 > 0

def is_hexagonal_number(n):
    # H = n(2n - 1)
    # 2n^2 - n - H 
    v1, _ = solve_quadratic(2, -1, -n)

    return v1.is_integer() and v1 > 0

# generate first n triangular numbers
values = {n * (n + 1) / 2 for n in range(100000)}
values = {n for n in values if is_pentagonal_number(n) and is_hexagonal_number(n)}

print(sorted(values))