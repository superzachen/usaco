# USACO 2014 December Contest, Bronze: Problem 1 - Marathon

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=487)

## Problem Description

Bessie must run through N checkpoints in sequence, starting at checkpoint 1 and finishing at checkpoint N. She wants to minimize her total distance by skipping up to one checkpoint (but cannot skip the start or finish). The distance between checkpoints uses Manhattan distance: |x1-x2| + |y1-y2|.

## Input Format

- First line: integer N (3 ≤ N ≤ 100,000)
- Next N lines: two space-separated integers x and y for each checkpoint (-1000 ≤ x, y ≤ 1000)

## Output Format

A single integer representing the minimum distance Bessie can run by skipping up to one checkpoint.

## Sample Input

```
4
0 0
8 3
11 -1
10 0
```

## Sample Output

```
14
```

## Explanation

The optimal solution involves skipping the checkpoint at coordinates (8, 3). This results in the path: (0,0) → (11,-1) → (10,0), which totals 14 units of distance using Manhattan distance calculations.
