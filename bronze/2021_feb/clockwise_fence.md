# USACO 2021 February Contest, Bronze: Problem 3 - Clockwise Fence

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=1109)

## Problem Description

Farmer John is laying out a new fence that follows an irregular path described by directional characters (N, E, S, W), each representing a 1-meter run. The fence returns to its starting point, enclosing a connected region. The task is to determine whether the fence path travels clockwise (with the enclosed region on the right) or counterclockwise (with the enclosed region on the left).

## Input Format

The first line contains an integer N (1 ≤ N ≤ 20). Each of the next N lines contains a string of length 4-100 describing a fence path using characters N, E, S, and W.

## Output Format

For each fence path, output either "CW" (clockwise) or "CCW" (counterclockwise).

## Sample Input

```
2
NESW
WSSSEENWNEESSENNNNWWWS
```

## Sample Output

```
CW
CCW
```
