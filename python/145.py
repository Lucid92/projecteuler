# This solution is quite slow, im obviously missing something but every optimisation
# I tried makes it slow. Eg I realise im checking x and revserse(x) which isn't needed
# by my methods for fixing this were making it slower.

def reverse(n):
    v = 0
    place = 1
    for i in get_digits(n)[::-1]:
        v += i * place
        place *= 10

    return v

def get_digits(n):
    digits = []
    while n:
        digits.append(n % 10)
        n //= 10

    return digits

def is_reversable(n):
    digits = get_digits(n)

    carry = 0

    for i in range(len(digits)):
        v = digits[i] + digits[len(digits) - i - 1] 
        if (v + carry) % 2 == 0:
            return False

        if v >= 10:
            carry = 1
        else:
            carry = 0

    return True

c = 0
for i in range(1, 1_000_000_000):
    if i % 10 == 0:
        continue
    # r = reverse(i)
    # if r < i:
    #     if r in truthies:
    #         c+=1
    #     continue
    
    if is_reversable(i):
        c+=1

print(c)