# https://usaco.org/index.php?page=viewproblem2&cpid=1491
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

input = sys.stdin.readline

n, q = read_ints()
grid = [list(input().strip()) for _ in range(n)]
canonical = [[0] * (n // 2) for _ in range(n // 2)]
ans = 0

def apply(x, y, scale):
    if grid[x][y] == '.':
        return
    x = min(x, n - 1 - x)
    y = min(y, n - 1 - y)
    ans -= min(canonical[x][y], 4 - canonical[x][y])
    canonical[x][y] += scale
    ans += min(canonical[x][y], 4 - canonical[x][y])

for i in range(n):
    for j in range(n):
        apply(i, j, 1)

print(ans)
for _ in range(q):
    x, y = read_ints()
    x -= 1
    y -= 1
    apply(x, y, -1)
    grid[x][y] = '#' if grid[x][y] == '.' else '.'
    apply(x, y, 1)
    print(ans)