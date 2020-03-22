import math

def get_chain_length(n):
    previous_values = set([n])

    while True:
        n = factorial_sum(n)
        if n in previous_values:
            break

        previous_values.add(n)
    
    return len(previous_values)

def factorial_sum(n):
    return sum(math.factorial(int(i)) for i in str(n))

sixty_count = 0

for i in range(69, 1000000):
    length = get_chain_length(i)

    if length == 60:
        sixty_count += 1

print(sixty_count)