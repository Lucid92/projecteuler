# Every "square" of the spiral is 4 values to add to the sum.
# Difference between each value in an a square is 2n where n is the square count.

def solve(size):
    # middle value
    result = 1
    spiral_val = 1

    for sq in range(1, size // 2 + 1): # size / 2 since for a 5x5 grid, there are 3 squares.
        for _ in range(4):
            spiral_val += 2 * sq
            result += spiral_val

    return result

print(solve(1001))