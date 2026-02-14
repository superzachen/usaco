# https://usaco.org/index.php?page=viewproblem2&cpid=1347
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

    
n = (read_ints())[0]
cows = read_ints()
canes = read_ints()
    
for cane_height in canes:
    current_base = 0
    current_top = cane_height
        
    for i in range(n):
        if cows[i] > current_base:
            eat_to = min(cows[i], current_top)
            amount_eaten = eat_to - current_base
            cows[i] += amount_eaten
            current_base = eat_to
        if current_base >= current_top:
            break
for h in cows:
    print(h)