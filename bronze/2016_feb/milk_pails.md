# USACO 2016 February Contest, Bronze: Problem 1 - Milk Pails

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=615)

## Problem Description

Farmer John needs to fill exactly M units of milk using three pails of sizes X, Y, and M (where 1 ≤ X < Y < M). All pails start empty. He can perform two operations:
- Fill the X-sized pail and pour it into the M-sized pail (if no overflow)
- Fill the Y-sized pail and pour it into the M-sized pail (if no overflow)

The goal is to determine the maximum milk that can be added to the M-sized pail.

## Input Format

A single line containing three space-separated integers: X, Y, and M.

## Output Format

A single integer representing the maximum amount of milk that can be added to the M-sized pail.

## Sample Input

```
17 25 77
```

## Sample Output

```
76
```

## Explanation

FJ fills the pail of size 17 three times and the pail of size 25 once, accumulating a total of 76 units of milk (3 × 17 + 1 × 25 = 76).
