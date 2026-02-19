# https://usaco.org/index.php?page=viewproblem2&cpid=1204
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

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

pos_in_B = [0]*(N+1)
for i in range(N):
	pos_in_B[B[i]] = i+1

A = [pos_in_B[v] for v in A]
# now assume B=1...N

max_so_far = 0
ans = 0
 
for a in A:
	if a > max_so_far:
		max_so_far = a
	else:  # max_so_far remains the same
		ans += 1
 
print(ans)