# https://usaco.org/index.php?page=viewproblem2&cpid=1299
import sys
import os

problem_name = "hungry_cow"

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

N, T = read_ints()
deliver = []
for _ in range(N):
    D, A = read_ints()
    deliver.append([D, A])
Ans = 0
Haybles = 0
for i in range(1, T+1):
    for delivery in deliver:
        if delivery[0] == i:
            Haybles += (delivery[1])
    if Haybles >= 1:
        Ans += 1
        Haybles -= 1
print(Ans)