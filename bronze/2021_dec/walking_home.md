# USACO 2021 December Contest, Bronze: Problem 3 - Walking Home

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=1157)

## Problem Description

Bessie the cow must travel from the top-left corner to the bottom-right corner of an N×N grid. She can only move down or right, and must navigate around haybales blocking certain squares. Her key constraint is that she can change direction at most K times during her journey.

## Input Format

- First line: T (number of test cases, 1 ≤ T ≤ 50)
- For each test case:
  - Line 1: N and K (2 ≤ N ≤ 50, 1 ≤ K ≤ 3)
  - Next N lines: N-character strings using '.' for empty squares and 'H' for haybales

## Output Format

For each test case, output a single integer representing the count of distinct valid paths from start to finish.

## Sample Input

```
7
3 1
...
...
...
3 2
...
...
...
3 3
...
...
...
3 3
...
.H.
...
3 2
...
HH.
...
3 3
...
HH.
...
4 3
....
.H..
..H.
....
```

## Sample Output

```
2
4
6
2
0
0
6
```
