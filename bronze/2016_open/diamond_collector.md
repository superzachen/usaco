# USACO 2016 US Open Contest, Bronze: Problem 1 - Diamond Collector

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=639)

## Problem Description

Bessie the cow collects N diamonds of varying sizes and wants to display some in a case. She has a constraint: "she will not include two diamonds in the case if their sizes differ by more than K." The task is to find the maximum number of diamonds that can be displayed together while respecting this size constraint.

## Input Format

- First line: Two integers N and K (where N ≤ 1000 and 0 ≤ K ≤ 10,000)
- Next N lines: Each contains an integer representing a diamond's size (positive integers ≤ 10,000)

## Output Format

A single integer representing the maximum number of diamonds that can be displayed.

## Sample Input

```
5 3
1
6
4
3
1
```

## Sample Output

```
4
```

## Solution Approach

The optimal strategy involves sorting the diamonds by size, then using a sliding window to find the longest contiguous subsequence where the difference between the largest and smallest diamond doesn't exceed K.
