ways = 0

def give_change(target, values):
    global ways

    for v in values:
        new_target = target - v
        if new_target < 0:
            return
        if new_target == 0:
            ways += 1
            return
        else:
            # to get combinations rather than permutations.
            new_values = values[0:values.index(v) + 1]
            give_change(new_target, new_values)

v = [1, 2, 5, 10, 20, 50, 100, 200]
give_change(200,v)

print(ways)

