# https://usaco.org/index.php?page=viewproblem2&cpid=1325
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

# Read in the input
N, K, T = read_ints()
A = read_ints() + [N] # append the value N to the sequence

ans = [-1] * N # declare an empty final array

for i in range(K):
    for j in range(A[i], A[i+1]):
        T_prime = T-(j-A[i]+1)

        if T_prime >= 0:
            increase_times = 1 + T_prime // (A[i+1]-A[i]) # integer division is // in python
            ending_position = (j + increase_times * (A[i+1]-A[i])) % N
        else:
    		# doesn't move at all
            ending_position = j

        ans[ending_position] = j

# Print the output
print(" ".join(map(str, ans)))