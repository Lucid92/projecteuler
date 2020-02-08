def solve(size):
    # The size given in the question is the size of the lattice in squares, we need the size in nodes.
    size += 1 

    # default as 1 since we are starting in the bottom right corner, and all the other values will be overwritten anyway.
    grid = [[1 for y in range(size)] for x in range(size)]

    # bottom row is already filled in correctly (only 1 path), so start on the 2nd bottom row.
    for y in range(size - 2, -1, -1):
        for x in range(size - 1, -1, -1):
            right_val = grid[x + 1][y] if  x + 1 < size else 0
            down_val = grid[x][y + 1] if  y + 1 < size else 0

            grid[x][y] = right_val + down_val

    return grid[0][0]

print(solve(20))