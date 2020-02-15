def make_divisible(n, d):
    while n // d == 0:
        n *= 10

    return n

def find_repeating_period(dividend, divisor):
    # Use long division to find the period of the repeating decimals.
    dividend = make_divisible(dividend, divisor)
    previous_interations = []

    while True:        
        previous_interations.append((dividend, divisor))
        remainder = dividend % divisor

        if remainder == 0:
            period = 0
            break

        dividend = make_divisible(remainder, divisor)

        if (dividend, divisor) in previous_interations:
            period = len(previous_interations) - previous_interations.index((dividend, divisor))
            break

    return period

longest_cycle = 0
d = 0

for i in range(2, 1000):
    val = find_repeating_period(1, i)

    if val > longest_cycle:
        longest_cycle = val
        d = i

print(longest_cycle, d)