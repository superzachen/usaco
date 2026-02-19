# https://usaco.org/index.php?page=viewproblem2&cpid=1348
import sys
import os
import math
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


def main():
    n = read_int()
    s = read_ints()
    segments = []
    region = 0
    for i in range(n):
        if s[i] == '1':
            region += 1
        else:
            if region > 0:
                segments.append(region)
            region = 0
    if region > 0:
        segments.append(region)
    num_infected = n
    window = 1
    while window <= n:
        temp_infected = 0
        for i, block in enumerate(segments):
            if (i == 0 and s[0] == '1') or (i == len(segments) - 1 and s[n-1] == '1'):
                if window > block * 2 - 1:
                    print(num_infected)
                    return
            else:
                if window > block:
                    print(num_infected)
                    return
            temp_infected += (block + window - 1) // window
        num_infected = min(num_infected, temp_infected)
        window += 2
    print(num_infected)

if __name__ == "__main__":
    main()