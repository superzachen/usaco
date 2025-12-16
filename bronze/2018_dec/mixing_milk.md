# USACO 2018 December Contest, Bronze: Problem 1 - Mixing Milk

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=855)

## Problem Description

Farmer John has three buckets of milk from his cows Bessie, Elsie, and Mildred. He performs a cyclic pouring sequence: bucket 1 into bucket 2, then bucket 2 into bucket 3, then bucket 3 into bucket 1, repeating this pattern for 100 total pour operations. Each pour transfers as much milk as possible until either the source bucket empties or the destination bucket fills.

## Input Format

Three lines follow, each containing two space-separated integers representing a bucket's capacity and current milk amount. Both values are positive, at most 1 billion, with capacity ≥ milk amount.

## Output Format

Three lines showing the final milk amount in each bucket after completing all 100 pours.

## Sample Input

```
10 3
11 4
12 5
```

## Sample Output

```
0
10
2
```

## Sample Walkthrough

The example demonstrates the pouring sequence beginning from initial state (3, 4, 5):
- Pour 1→2: (0, 7, 5)
- Pour 2→3: (0, 0, 12)
- Pour 3→1: (10, 0, 2)
- Pour 1→2: (0, 10, 2)
- Pour 2→3: (0, 0, 12)

The pattern then cycles through the last three states repeatedly.
