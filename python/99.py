import math

# a**b > c**d?
# log_a(x) = b             log_c(y) = d
# log_c(x) / log_c(a) = b  log_c(y) = d
# log_c(x) = b * log_c(a)  log_c(y) = d
# therefore if b * log_c(a) > d then c > y and a**b > c**d.

# parameter names arent ideal but are based of the example above.
def compare(a:int, b:int, c:int, d:int) -> bool:
    ''' Returns true if a**b > c**d '''
    return b * math.log(a, c) > d

with open("p099_base_exp.txt", "r") as file:
    max_line = 0
    max_pair = (2, 2)
    for i, pair in enumerate(file.readlines()):
        a, b = (int(v) for v in pair.split(","))

        if compare(a, b, max_pair[0], max_pair[1]):
            max_line = i + 1
            max_pair = (a, b)

    print(max_line, max_pair)

