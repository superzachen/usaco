# https://usaco.org/index.php?page=viewproblem2&cpid=1492
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

N = read_int()
a = read_ints()

cnt = [0] * (N + 1)
for x in a:
    cnt[x] += 1

missing_lt_i = 0
for i in range(N + 1):
    print(max(cnt[i], missing_lt_i))
    missing_lt_i += cnt[i] == 0
