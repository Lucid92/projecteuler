def conc_product(i, n):
    conc = ""
    for r in range(n):
        conc += str(i * (r + 1))

    return int(conc)

def is_pandigital(n):
    n_str = str(n)
    return len(set(n_str)) == len(n_str)

pandigitals = []

# i is limited to < 10000 since 10000 * 1 concat 10000 * 2 = 1000020000.
for i in range(1, 10000):
    # n is limited to < 10 since 1 * 1 concat 1 * 2 concat ... concat 1 * 10 = 12345678910.
    for n in range(1, 9):
        res = conc_product(i, n)
        if is_pandigital(res) and '0' not in str(res):
            pandigitals.append(res)

print(max(pandigitals))
