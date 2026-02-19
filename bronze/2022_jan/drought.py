# https://usaco.org/index.php?page=viewproblem2&cpid=1181
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

def solve(H):
    N = len(H)
    f = 0
    for i in range(N):
        f += (1 if i % 2 == 0 else -1) * H[i]
    if N % 2 == 0:
        if f != 0:
            return -1
    else:
        if f < 0:
            return -1
    last_o = 0
    o = [0] * (N - 1)
    for i in range(N - 1):
        last_o = o[i] = H[i] - f - last_o
        if o[i] < 0:
            return -1
    if N % 2 == 0:
        mn = o[0]
        for i in range(0, N, 2):
            mn = min(mn, o[i])
        for i in range(0, N, 2):
            o[i] -= mn
    sum_o = sum(o)
    return 2 * sum_o


t = int(input())
for _ in range(t):
    N = int(input())
    H = list(map(int, input().split()))
    print(solve(H))