# USACO 2015 December Contest, Bronze: Problem 1 - Fence Painting

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=567)

## Problem Description

Farmer John and his cow Bessie are repainting a fence. Farmer John paints an interval from x=a to x=b, while Bessie independently paints from x=c to x=d. These intervals may overlap partially or completely. The task is to determine the total length of fence covered by paint.

## Input Format

Two lines:
- Line 1: integers a and b separated by a space, where a < b
- Line 2: integers c and d separated by a space, where c < d

All values fall within the range 0 to 100, inclusive.

## Output Format

A single line containing the total length of fence covered with paint.

## Sample Input

```
7 10
4 8
```

## Sample Output

```
6
```

## Sample Explanation

The painted intervals are [7, 10] and [4, 8]. These overlap from x=7 to x=8. The union covers from x=4 to x=10, yielding a total length of 6 units.
