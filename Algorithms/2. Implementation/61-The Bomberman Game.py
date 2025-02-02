# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/bomber-man/problem?isFullScreen=true


# Language: Python

# ========================
#         Solution
# ========================

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#

def bomberMan(n, grid):
    if n == 1: 
        return grid
        
    # The grid is totally full on every other turn
    if n % 2 == 0:
        return ["O" * len(grid[0]) for _ in range(len(grid))]
    
    countdown_grid = []
    for row in grid:
        countdown_row = [2 if cell == "O" else -1 for cell in row]
        countdown_grid.append(countdown_row)
    
    planting_this_turn = True

    num_iterations = ((n-2) % 4) + 1 
    for i in range(num_iterations):
        # planting
        if planting_this_turn:
            new_countdown_grid = []
            for row in countdown_grid:
                # 4 because we will decrement the counter this turn
                new_countdown_row = [4 if cell == -1 else cell for cell in row]
                new_countdown_grid.append(new_countdown_row)
            countdown_grid = new_countdown_grid
        
        # countdown
        bombs_to_detonate = []
        for row in range(len(countdown_grid)):
            for col in range(len(countdown_grid[0])):
                countdown_grid[row][col] -= 1
                if countdown_grid[row][col] == 0:
                    bombs_to_detonate.append((row, col))
                
        # explosion
        for bomb in bombs_to_detonate:
            row, col = bomb
            countdown_grid[row][col] = -1
            
            if 0 < col: # left
                countdown_grid[row][col-1] = -1
                
            if 0 < row: # top
                countdown_grid[row - 1][col] = -1
            
            if col < len(countdown_grid[row]) - 1: # right
                countdown_grid[row][col + 1] = -1
            
            if row < len(countdown_grid) - 1: # bottom
                countdown_grid[row + 1][col] = -1
        
        planting_this_turn = not planting_this_turn
        
    final_grid = []
    for row in countdown_grid:
        str_array = ["." if cell == -1 else "O" for cell in row]
        s = "".join(str_array)
        final_grid.append(s)
    
    return final_grid
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
