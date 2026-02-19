# https://usaco.org/index.php?page=viewproblem2&cpid=1205
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

def solve():
    n = int(input())
    l = [input() for _ in range(4)]
    words = set()
    for a in range(4):
        for b in range(4):
            if a in [b]:
                continue
            for c in range(4):
                if c in [a, b]:
                    continue
                for d in range(4):
                    if d in [a, b, c]:
                        continue
                    for l1 in l[a]:
                        words.add(l1)
                        for l2 in l[b]:
                            words.add(l1+l2)
                            for l3 in l[c]:
                                words.add(l1+l2+l3)
                                for l4 in l[d]:
                                    words.add(l1+l2+l3+l4)
    for _ in range(n):
        print("YES" if input() in words else "NO")
 
solve()