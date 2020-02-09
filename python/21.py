
import lib.mathhelper as mathhelper

def solve(bound):
    # maps the sum of the proper divisors to the original n value.
    sum_map = []

    for i in range(bound):
        div_sum = sum(mathhelper.get_proper_divisors(i))
        sum_map.append(div_sum) 

    result = 0
    for i, div_sum in enumerate(sum_map):
        if div_sum > bound:
            continue

        if sum_map[div_sum] == i and sum_map[i] != i:            
            result += i

    return result

print(solve(10000))

