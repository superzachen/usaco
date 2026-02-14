# https://usaco.org/index.php?page=viewproblem2&cpid=487
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

point_lis = []
for i in range(N):
    point_lis.append(read_ints())

def dist(x1, y1, x2, y2):
    return(abs(x1 - x2) + abs(y1 - y2))

def calc_total(points):
    total = 0
    for i in range(len(points) - 1):
        total += dist(points[i][0], points[i][1], points[i + 1][0], points[i + 1][1])
    return(total)

cases = []
for i in range(1, len(point_lis)-1):
    new_lis = point_lis[:i] + point_lis[i+1:]
    cases.append(calc_total(new_lis))

print(min(cases))