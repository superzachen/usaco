# https://usaco.org/index.php?page=viewproblem2&cpid=1229
import sys
from sys import stdin
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

def main():
    input = stdin.readline
    n = int(input())
    have = list(map(int, input().split()))
    k = int(input())
    need = [[] for _ in range(n)]
    for _ in range(k):
        want, m = map(int, input().split())
        want -= 1
        need[want] = [x - 1 for x in map(int, input().split())]

    ret = 0
    while True:
        consume = [0] * n
        consume[n-1] += 1
        good = True
        for i in range(n-1, -1, -1):
            if consume[i] <= have[i]:
                have[i] -= consume[i]
                continue
            if len(need[i]) == 0:
                good = False
                break
            take = min(consume[i], have[i])
            consume[i] -= take
            have[i] -= take
            for out in need[i]:
                consume[out] += consume[i]
        if good:
            ret += 1
        else:
            break
    print(ret)

if __name__ == "__main__":
    main()