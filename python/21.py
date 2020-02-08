def get_proper_divisors(n):
    ''' Finds the proper divisors of input n where
    a proper divisor is any number less than n that divides n evenly'''

    # any numbers > n / 2 can't be proper divisors
    return [i for i in range(1, n // 2 + 1) if n % i == 0]

def solve(bound):
    # maps the sum of the proper divisors to the original n value.
    sum_map = []

    for i in range(bound):
        div_sum = sum(get_proper_divisors(i))
        sum_map.append(div_sum) 

    result = 0
    for i, div_sum in enumerate(sum_map):
        if div_sum > bound:
            continue

        if sum_map[div_sum] == i and sum_map[i] != i:            
            result += i

    return result

print(solve(10000))

