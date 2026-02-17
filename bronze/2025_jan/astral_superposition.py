# https://usaco.org/index.php?page=viewproblem2&cpid=1467
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

input_data = sys.stdin.read().split()
n = int(input_data[0])
# The remaining data contains the target grid followed by the pattern grid
grid_data = input_data[1:]

target_grid = grid_data[:n]
pattern_grid = grid_data[n:2*n]

# 1. Store coordinates of '#' in the target
target_hashes = set()
for r in range(n):
    for c in range(n):
        if target_grid[r][c] == '#':
            target_hashes.add((r, c))

# 2. Store coordinates of '#' in the pattern
pattern_hashes = []
for r in range(n):
    for c in range(n):
        if pattern_grid[r][c] == '#':
            pattern_hashes.append((r, c))

# 3. Pre-calculate all "Legal" shifts
# A shift is legal if no pattern '#' lands on a target '.'
valid_shifts_coverage = []

for dr in range(-(n - 1), n):
    for dc in range(-(n - 1), n):
        is_legal = True
        current_coverage = set()
        
        for r, c in pattern_hashes:
            nr, nc = r + dr, c + dc
            # If the shifted coordinate is within the grid boundaries
            if 0 <= nr < n and 0 <= nc < n:
                if target_grid[nr][nc] == '.':
                    is_legal = False
                    break
                current_coverage.add((nr, nc))
        
        if is_legal:
            valid_shifts_coverage.append(current_coverage)

# 4. Try combining two legal shifts to see if they cover the target perfectly
found = False
num_shifts = len(valid_shifts_coverage)

for i in range(num_shifts):
    for j in range(i, num_shifts):
        # Union of the two sets of covered coordinates
        if (valid_shifts_coverage[i] | valid_shifts_coverage[j]) == target_hashes:
            found = True
            break
    if found:
        break

# 5. Output the result
if found:
    print("YES")
else:
    print("NO")