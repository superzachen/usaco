# https://usaco.org/index.php?page=viewproblem2&cpid=1349
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

def ceilingDiv(a, b):
    return (a + b - 1) // b
 
def solve():
    n = read_int()
    h = [int(x) for x in read_int()]
    a = [int(x) for x in read_int()]
    t = [int(x) for x in read_int()]
    ord = [i for i in range(n)]
    ord.sort(key=lambda x: t[x])
    ret = 0
    for ordi in range(n-1):
        i = ord[ordi]
        j = ord[ordi+1]
        if h[i] < h[j] and a[i] > a[j]:
            ret = max(ret, ceilingDiv(h[j] - h[i] + 1, a[i] - a[j]))
    for i in range(n):
        h[i] += a[i] * ret
    for ordi in range(n-1):
        i = ord[ordi]
        j = ord[ordi+1]
        if h[i] <= h[j]: return -1
    return ret
 
t = read_int()
for _ in range(t):
    print(solve())