import math
def count_solutions(p):
    solutions = 0

     # The longest a side can be is p / 2 since p = a + b + sqrt(a^2 + b^2). If a or b are zero then p = 2a for instance.
    upper_bound = math.ceil(p / 2)

    for a in range(1, upper_bound):
        for b in range(1, upper_bound):
            if a + b + math.sqrt(a**2 + b**2) == p:
                solutions += 1

    return solutions

max_solutions = 0
max_p = 0

for p in range(1001):
    solutions = count_solutions(p)
    if max_solutions < solutions:
        max_solutions = solutions
        max_p = p

print(max_solutions, max_p)