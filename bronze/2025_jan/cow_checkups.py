# https://usaco.org/index.php?page=viewproblem2&cpid=1469
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

n = read_int()
A = read_ints()
B = read_ints()

Same = sum(1 for i in range(n) if A[i] == B[i])
ans = [0] * (n + 1)

def expand(i, r):
    match = Same
    while i >= 0 and r < n:
        match += ((A[i] == B[r]) + (A[r] == B[i])) - ((A[i] == B[i]) + (A[r] == B[r]))
        ans[match] += 1
        i -= 1
        r += 1

for mid in range(n):
    expand(mid, mid)
    expand(mid, mid + 1)

for answer in ans:
    print(answer)