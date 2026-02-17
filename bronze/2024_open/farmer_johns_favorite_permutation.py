# https://usaco.org/index.php?page=viewproblem2&cpid=1421
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

def solve():
    N = int(input())
    H = list(map(int, input().split()))
    if H[-1] != 1:
        print(-1)
        return
    H = H[:-1]
    remaining = [False] + [True] * N
    for h in H:
        if not remaining[h]:
            print(-1)
            return
        remaining[h] = False
    ends = [x for x in range(1, N + 1) if remaining[x]]
    ans = [-1] * N
    l, r = 0, N - 1
    ans[l], ans[r] = ends
    for h in H:
        if ans[l] > ans[r]:
            l += 1
            ans[l] = h
        else:
            r -= 1
            ans[r] = h
    print(" ".join(map(str, ans)))
 
 
T = int(input())
for _ in range(T):
    solve()