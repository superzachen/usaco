# https://usaco.org/index.php?page=viewproblem2&cpid=1396
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

N, M = read_ints()
S = read_str()
A = read_ints()
 
ans = sum(A)
 
for i in range(N):
    if (S[i] == 'R' and S[(i + 1) % N] == 'L'):
        j = (i - 1 + N) % N 
        total = 0
 
        while S[j] == 'R':
            total += A[j]
            j = (j - 1 + N) % N 
 
        ans -= min(total, M)
    
    if (S[i] == 'L' and S[(i - 1 + N) % N] == 'R'):
        j = (i + 1) % N 
        total = 0
 
        while S[j] == 'L':
            total += A[j]
            j = (j + 1) % N 
 
        ans -= min(total, M)
 
print(ans)