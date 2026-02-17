# https://usaco.org/index.php?page=viewproblem2&cpid=1444
import sys
import os

problem_name = "xxx"

input_file = f"{problem_name}.in"
output_file = f"{problem_name}.out"

if os.path.exists(input_file):
    sys.stdin = open(input_file, "r")
    sys.stdout = open(output_file, "w")


def read_int():
    """Reads a single integer from a line."""
    return int(sys.stdin.readline())


def read_str():
    """Reads a single string from a line."""
    return sys.stdin.readline().strip()


def read_ints():
    """Reads multiple integers from a line, separated by space."""
    return list(map(int, sys.stdin.readline().split()))


def read_strs():
    """Reads multiple strings from a line, separated by space."""
    return sys.stdin.readline().split()

n, q = read_ints()

# We need to track how many blocks are carved in each 'column' across 3 planes
# Using 2D lists. Since N can be 1000, N*N is 1 million.
count_xy = [[0] * n for _ in range(n)]
count_xz = [[0] * n for _ in range(n)]
count_yz = [[0] * n for _ in range(n)]

total_bricks = 0
results = []

# Pointer for input data
idx = 2
for _ in range(q):
    x, y, z = read_ints()
    idx += 3
    
    # 1. Check Z-axis orientation (fixed x, y)
    count_xy[x][y] += 1
    if count_xy[x][y] == n:
        total_bricks += 1
        
    # 2. Check Y-axis orientation (fixed x, z)
    count_xz[x][z] += 1
    if count_xz[x][z] == n:
        total_bricks += 1
        
    # 3. Check X-axis orientation (fixed y, z)
    count_yz[y][z] += 1
    if count_yz[y][z] == n:
        total_bricks += 1
        
    results.append(str(total_bricks))