# USACO 2016 December Contest, Bronze: Problem 1 - Square Pasture

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=663)

## Problem Description

Farmer John wants to replace two rectangular pastures with a single square pasture that covers all previously enclosed areas. The square must have sides parallel to the x and y axes, and its area should be minimized.

## Input Format

Two lines, each containing four space-separated integers representing a rectangular pasture:
- `x1 y1 x2 y2` where (x1, y1) is the lower-left corner and (x2, y2) is the upper-right corner
- All coordinates are in range 0 to 10
- x2 > x1 and y2 > y1
- The two rectangles do not overlap or touch

## Output Format

A single integer representing the minimum area of a square pasture that encloses both rectangles.

## Sample Input

```
6 6 8 8
1 8 4 9
```

## Sample Output

```
49
```

## Explanation

The first rectangle spans from (6,6) to (8,8), and the second from (1,8) to (4,9). A square with side length 7 positioned at corners (1,6) and (8,13) covers both rectangles with minimum area of 49.
