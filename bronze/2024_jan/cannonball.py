# https://usaco.org/index.php?page=viewproblem2&cpid=1372
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

n, x = map(int, input().split())
pad = [(0, 0)] * (n + 1)
pad = [tuple(map(int, input().split())) for _ in range(n + 1)]
pad[0] = (0, 0)  # to keep indexing consistent with C++ code

vis = [False] * (n + 1)
dir = 1
power = 1
ans = 0

for _ in range(5000000):
    if not (1 <= x <= n):
        break
    if pad[x][0] == 1 and power >= pad[x][1] and not vis[x]:
        vis[x] = True
        ans += 1
    if pad[x][0] == 0:
        dir *= -1
        power += pad[x][1]
    x += dir * power

print(ans)