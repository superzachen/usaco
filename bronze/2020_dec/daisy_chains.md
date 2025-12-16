# USACO 2020 December Contest, Bronze: Problem 2 - Daisy Chains

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=1060)

## Problem Description

Bessie visits a pasture with N flowers labeled 1 to N, each having a certain number of petals. For every contiguous pair of flowers (i,j) where 1 ≤ i ≤ j ≤ N, Bessie photographs all flowers in that range. A photo has an "average flower" if at least one flower in the photo has a petal count equal to the average number of petals in that photo. The task is to count how many photos contain an average flower.

## Input Format

- First line: N (number of flowers, where 1 ≤ N ≤ 100)
- Second line: N space-separated integers representing petals per flower (1 ≤ petals ≤ 1000)

## Output Format

A single integer representing the count of photos that contain an average flower.

## Sample Input

```
4
1 1 2 3
```

## Sample Output

```
6
```

## Sample Explanation

All four single-flower photos qualify (each flower is trivially the average of itself). Additionally, the ranges (1,2) and (2,4) contain flowers matching their respective photo averages, bringing the total to 6.
