import math

# another boring solution thanks to python, maybe I should try these in another language one day...

digits = str(math.factorial(100))
solution = sum(int(digit) for digit in digits)

print(solution)