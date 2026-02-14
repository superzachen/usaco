# https://usaco.org/index.php?page=viewproblem2&cpid=1468
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
stream = read_ints()
total_remaining = [0] * (N + 1)
for val in stream:
    total_remaining[val] += 1
 
seen_on_left = [0] * (N + 1)
total_moos = 0
unique_chars_seen = 0
 
for i in range(N):
    current_val = stream[i]
    if total_remaining[current_val] == 2:
        is_b_already_in_prefix = (seen_on_left[current_val] > 0)
        total_moos += unique_chars_seen - is_b_already_in_prefix
    total_remaining[current_val] -= 1
    
    if seen_on_left[current_val] == 0:
        unique_chars_seen += 1 
        
    seen_on_left[current_val] += 1
 
print(total_moos)