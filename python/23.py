import lib.mathhelper as mathhelper
import itertools

def is_abundant_number(n):
    return sum(mathhelper.get_proper_divisors(n)) > n

# upper and lower bounds given by question.
abundant_numbers = [i for i in range(12, 28123 - 12 + 1) if is_abundant_number(i)]

sums = {sum(i) for i in itertools.combinations_with_replacement(abundant_numbers, 2)}

print(sum([i for i in range(28123) if i not in sums]))