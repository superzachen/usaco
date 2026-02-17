# https://usaco.org/index.php?page=viewproblem2&cpid=1420
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

N, P = read_ints()
fence_posts = [tuple(map(int, input().split())) for _ in range(P)]
label = [[-1] * 1001 for _ in range(1001)]
perimeter = 0


def walk_segment(start, end):  # walk from start to end one unit at a time
    global perimeter
    assert (start[0] == end[0]) + (start[1] == end[1]) == 1
    dif = end[0] - start[0], end[1] - start[1]
    dist = abs(dif[0]) + abs(dif[1])
    dif = dif[0] // dist, dif[1] // dist
    for _ in range(dist):
        assert label[start[0]][start[1]] == -1
        label[start[0]][start[1]] = perimeter
        perimeter += 1
        start = start[0] + dif[0], start[1] + dif[1]
    assert start == end


for i in range(P):
    walk_segment(fence_posts[i], fence_posts[(i + 1) % P])

for _ in range(N):
    x1, y1, x2, y2 = read_ints()
    p1 = label[x1][y1]
    p2 = label[x2][y2]
    dist = abs(p2 - p1)
    dist = min(dist, perimeter - dist)
    print(dist)