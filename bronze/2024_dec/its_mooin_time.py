# https://usaco.org/index.php?page=viewproblem2&cpid=1445
import sys
import os
from collections import defaultdict
from string import ascii_lowercase
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

N, F = read_ints()
S = read_str()
oc = defaultdict(int)
 
def is_moo(s):
	assert len(s) == 3
	return s[0] != s[1] == s[2]
 
for i in range(len(S)-2):
	s = S[i:i+3]
	if is_moo(s):
		oc[s] += 1
 
ans = set()
 
def add(pos, c, dif):
	for i in range(max(pos-2, 0), min(pos+1, len(S)-2)):
		s = list(S[i:i+3])
		s[pos-i] = c
		s_str = "".join(s)
		if is_moo(s_str):
			oc[s_str] += dif
			if oc[s_str] >= F:
				ans.add(s_str)
 
for i in range(len(S)):
	add(i, S[i], -1)
	for c in ascii_lowercase:
		add(i, c, 1)
		add(i, c, -1)
	add(i, S[i], 1)
 
ans = sorted(ans)
print(len(ans))
for m in ans:
	print(m)