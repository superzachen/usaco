# USACO 2025 February Contest, Bronze: Problem 1 - Reflection

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=1491)

## Problem Description

Farmer John creates a painting by dividing an N×N grid into four quadrants and painting in the top-right quadrant. He then reflects this design horizontally and vertically into the other three quadrants, creating a symmetric pattern.

After Bessie vandalizes the canvas by adding and removing painted cells, FJ needs to restore the reflective symmetry. The goal is to determine the minimum number of cell toggles (painting or removing paint) needed to restore the reflective condition.

A sequence of U updates modifies the canvas by toggling individual cells. Before applying any updates and after each update, the program must output the minimum operations required.

## Input Format

- Line 1: Two integers N and U (2 ≤ N ≤ 2000, N is even; 0 ≤ U ≤ 10⁵)
- Next N lines: N characters each representing the canvas (# for painted, . for unpainted)
- Next U lines: Two integers r and c (1 ≤ r, c ≤ N) indicating which cell to toggle

## Output Format

Output U+1 lines, each containing a single integer representing the minimum number of operations needed to satisfy the reflective condition before and after each update.

## Sample Input

```
4 5
..#.
##.#
####
..##
1 3
2 3
4 3
4 4
4 4
```

## Sample Output

```
4
3
2
1
0
1
```
