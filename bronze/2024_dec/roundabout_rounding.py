# https://usaco.org/index.php?page=viewproblem2&cpid=1443
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

def alg(N):
    digits = 0
    while 10**digits < N:
        digits += 1
    
    answer = 0
    for curdigits in range(1, digits+1):
        upper = int('5'+'0'*(curdigits-1))-1
        upper = min(N, upper)  
        lower = int('4'*curdigits)
        answer += max(0, upper - lower)
    return answer
 
T = read_int()
for _ in range(T):
    N = read_int()
    print(alg(N))
