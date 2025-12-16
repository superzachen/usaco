# USACO 2016 US Open Contest, Bronze: Problem 3 - Field Reduction

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=641)

## Problem Description

Farmer John needs to enclose N cows (where 3 ≤ N ≤ 50,000) positioned at distinct points in a 2D field with an axis-aligned rectangular fence. To minimize the enclosed area, he's willing to remove one cow from his herd before building the fence around the remaining N-1 cows.

Key constraints:
- Treat cows as points, not unit squares
- The fence consists of four line segments parallel to axes
- The area can be zero if remaining cows are collinear
- Cow locations are positive integers in range 1 to 40,000

## Input Format

First line contains N. The next N lines each contain two integers representing a cow's (x, y) coordinates.

## Output Format

A single integer representing the minimum area after optimally removing one cow.

## Sample Input

```
4
2 4
1 1
5 2
17 25
```

## Sample Output

```
12
```
