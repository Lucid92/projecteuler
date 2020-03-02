from decimal import Decimal

def cancel_digits(num, dem):
    '''Returns a tuple comtaining the numerator and denominater of a fraction where 
    if the input numerator and denominator share a digit, they are canceled.'''

    num_str = str(num)
    dem_str = str(dem)

    repl = None

    if num_str[0] in dem_str:
        repl = num_str[0]
    elif num_str[1] in dem_str:
        repl = num_str[1]

    if not repl:
        return None

    num_str = num_str.replace(repl, "")
    dem_str = dem_str.replace(repl, "")

    return (int(num_str), int(dem_str))

truthy = []

for dem in range(10, 100):
    for num in range(10, dem):
        # skip trivial or guaranteed false cases.
        if num == dem or num % 10 == 0 or dem % 10 == 0 or len(set(str(num))) == 1 or len(set(str(dem))) == 1:
            continue

        res = cancel_digits(num, dem)

        if not res:
            continue

        new_frac = res[0] / res[1]        

        if new_frac == num / dem:
            truthy.append((num, dem))

for n, d in truthy:
    print(f'{n}/{d}')