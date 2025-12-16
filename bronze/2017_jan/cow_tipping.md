# USACO 2017 January Contest, Bronze: Problem 3 - Cow Tipping

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=689)

## Problem Description

Farmer John has N² cows arranged in an N×N grid, some tipped over by teenagers. He has a machine called the "Cow-Untipperator 3000" that can flip cows in any upper-left rectangle (a rectangular sub-grid containing the upper-left cow). Each application toggles all cows in the selected rectangle. The goal is to restore all cows to upright position with the minimum number of machine applications.

Key constraints:
- 1 ≤ N ≤ 10
- Each upper-left rectangle can be used at most once (applying twice cancels out)
- 0 represents an upright cow, 1 represents a tipped cow

## Input Format

First line: integer N

Next N lines: strings of N characters (each '0' or '1')

## Output Format

Minimum number of applications needed to restore all cows to upright position

## Sample Input

```
3
001
111
111
```

## Sample Output

```
2
```

## Sample Explanation

Applying the machine to the entire 3×3 grid toggles all cows to:
```
110
000
000
```

Then applying the machine to the upper-left 2×2 rectangle completes the restoration. Total: 2 applications.
