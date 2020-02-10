def solve(digits):
    n = 2

    fnm1 = 1 # f(n - 1)
    fn = 1 # f(n)

    while len(str(fn)) < digits:
        tmp = fn
        fn += fnm1
        fnm1 = tmp

        n += 1

    return n

print(solve(1000))