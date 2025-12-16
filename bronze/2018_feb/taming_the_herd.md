# USACO 2018 February Contest, Bronze: Problem 3 - Taming the Herd

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=809)

## Problem Description

Farmer John tracks cow breakouts using a counter that shows days since the last breakout. On a breakout day, the counter reads 0; otherwise it shows how many days have passed since the most recent breakout.

Some log entries are missing (marked as -1). Farmer John knows a breakout definitely occurred on day 1. Given the partial log, determine the minimum and maximum possible number of breakouts that could have occurred.

## Input Format

- Line 1: Integer N (1 ≤ N ≤ 100), the number of logged days
- Line 2: N space-separated integers, where each is either -1 (missing entry) or a non-negative integer ≤ 100 (counter value on that day)

## Output Format

Output two space-separated integers: the minimum and maximum possible breakout counts. If no valid sequence exists consistent with the constraints, output -1.

## Sample Input

```
4
-1 -1 -1 1
```

## Sample Output

```
2 3
```

## Explanation

A breakout must occur on day 1 (given) and day 3 (since the counter reads 1 on day 4). The uncertainty is whether day 2 had a breakout, yielding either 2 or 3 total breakouts.
