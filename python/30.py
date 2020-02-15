# This will be the upper limit to the problem since 7 * 9 ** 5 is a 6 digit number.
upper_limit = 6 * 9**5

positives = []

# 1 doesnt count. I'm sure there's a obviously lower limit too but it's hardly an impact on performance.
for i in range(2, upper_limit):
    if i == sum(int(n) ** 5 for n in str(i)):
        positives.append(i)

print(sum(positives))
