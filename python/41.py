import itertools
import lib.mathhelper as mathhelper

# checked 9 digit and 8 digit manually
for i in itertools.permutations("7654321", 7):
    n = int(''.join(i))
    if mathhelper.is_prime(n):
        print(n)
        break