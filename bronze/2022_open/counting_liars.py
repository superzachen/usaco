# https://usaco.org/index.php?page=viewproblem2&cpid=1228
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

locations = []
for _ in range(N):
    dir = input().split()
    d = dir[0]
    x = int(dir[1])
    if d[0] == 'G':
        locations.append((x, -1))
    else:
        locations.append((x, 1))

minLiars = N
locations.sort()

for idx in range(N):
    numLiars = 0
    for jdx in range(idx):
        if locations[jdx][1] == 1:
            numLiars += 1
    for jdx in range(idx + 1, N):
        if locations[jdx][1] == -1:
            numLiars += 1
    minLiars = min(numLiars, minLiars)

print(minLiars)

