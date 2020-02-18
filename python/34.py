import math

n = 3
result_sum = 0

# I'm sure there's an upper limit here but this works.
while True:
    digits = [int(i) for i in str(n)]
    factorial_sum = sum(math.factorial(i) for i in digits)

    if factorial_sum == n:
        result_sum += factorial_sum
        print(n, result_sum)

    n += 1