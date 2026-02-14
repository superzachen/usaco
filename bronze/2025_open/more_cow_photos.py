# https://usaco.org/index.php?page=viewproblem2&cpid=1516
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

t = read_int()
for _ in range(t):
    n = read_int()
    cow_count = [0] * (n+1)
    cows = read_ints()
    for cow in cows:
        cow_count[cow] += 1
    final = 1
    canidate = 1
    for i in range(len(cow_count)):
        if cow_count[i] > 0:
            final = canidate
            if cow_count[i] >= 2:
                canidate += 2
    print(final)

            
               
    