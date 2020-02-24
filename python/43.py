import itertools

def is_pandigital(n):
    digits = str(n)
    return len(set(digits)) == len(digits) and len(digits) == 10

result = 0

for perm in list(itertools.permutations("0123456789", 10)):
    n = ''.join(perm)

    if n[0] == '0':
        continue

    if (int(n[1:4]) % 2 != 0 or
        int(n[2:5]) % 3 != 0 or 
        int(n[3:6]) % 5 != 0 or 
        int(n[4:7]) % 7 != 0 or 
        int(n[5:8]) % 11 != 0 or
        int(n[6:9]) % 13 != 0 or 
        int(n[7:10]) % 17 != 0):
        continue

    result += int(n)

print(result)
