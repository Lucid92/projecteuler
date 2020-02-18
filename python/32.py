def is_pandigital(n):
    digits = str(n)
    return len(set(digits)) == len(digits) and '0' not in digits

results = set()

for multiplicand in range(3000): 
    if not is_pandigital(multiplicand):
        continue

    for multiplier in range(3000):
        digit_collection = str(multiplicand) + str(multiplier)

        if not is_pandigital(multiplier):
            continue
        
        product = multiplicand * multiplier

        digit_collection += str(product)

        if is_pandigital(digit_collection) and len(digit_collection) == 9:
            results.add(product)

print(sum(results))