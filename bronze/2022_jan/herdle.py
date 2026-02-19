# https://usaco.org/index.php?page=viewproblem2&cpid=1179
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

def main():
    correct = input() + input() + input()
    guess = input() + input() + input()
    freq_correct = [0] * 26
    freq_guess = [0] * 26
    green = 0
    for j in range(9):
        if correct[j] == guess[j]:
            green += 1
        freq_correct[ord(correct[j]) - ord('A')] += 1
        freq_guess[ord(guess[j]) - ord('A')] += 1
    yellow = 0
    for j in range(26):
        yellow += min(freq_correct[j], freq_guess[j])
    yellow -= green
    print(green)
    print(yellow)

if __name__ == "__main__":
    main()