def get_binary_value(n):
    ''' Returns n in base 2 as a string.'''
    return bin(n)[2:] 

def is_palindrome(s):
    return s == s[::-1] 

truthy = [] 

for i in range(1000000):
    binary = bin(i)

    if is_palindrome(str(i)) and is_palindrome(get_binary_value(i)):
        truthy.append(i)

print(sum(truthy))