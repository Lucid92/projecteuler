def get_digit(n):
    number = 1
    position = 1    

    while position < n:
        number += 1
        position += len(str(number))

    offset = position - n

    number_str = str(number)

    return int(number_str[len(number_str) - 1 - offset])

vals = []

for i in range(7):
    vals.append(get_digit(10**i))

print(vals)

res = 1
for val in vals:
    res *= val

print(res)