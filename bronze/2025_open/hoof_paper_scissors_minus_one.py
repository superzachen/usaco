# https://usaco.org/index.php?page=viewproblem2&cpid=1515
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
data = [read_str() for _ in range(N)]
wins = [[0] * N for _ in range(N)]
 
for i in range(N):
    for j in range(i):
        if data[i][j] != "D":
            if data[i][j] == "W":
                wins[i][j] = 1
            else:
                wins[j][i] = 1
 
for _ in range(M):
    x, y = map(lambda x: int(x) - 1, read_ints())
    winning = 0
    for b in range(N):
        winning += wins[b][x] and wins[b][y]
    
    total_playable_pairs = N ** 2
    losing_pairs = (N-winning) ** 2
    
    print(total_playable_pairs - losing_pairs)