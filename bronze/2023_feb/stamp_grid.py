# https://usaco.org/index.php?page=viewproblem2&cpid=1300
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

T = read_int()
for _ in range(T):
    N = read_int()
    grid = [read_str() for _ in range(N)]
    K = read_int()
    stamp = [read_str() for _ in range(K)]
    ans = [['.' for _ in range(N)] for _ in range(N)]
    for rot in range(4):
        for i in range(N-K+1):
            for j in range(N-K+1):
                if all(grid[i+a][j+b] == '*' or stamp[a][b] == '.' for a in range(K) for b in range(K)):
                    for a in range(K):
                        for b in range(K):
                            if stamp[a][b] == '*':
                                ans[i+a][j+b] = '*'
        stamp = [[stamp[j][K-1-i] for j in range(K)] for i in range(K)]
    print("YES" if grid == ans else "NO")