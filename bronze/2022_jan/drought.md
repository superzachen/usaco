# USACO 2022 January Contest, Bronze: Problem 3 - Drought

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=1181)

## Problem Description

Farmer John has N cows arranged in a line, each with a hunger level hᵢ. The only way to decrease hunger is by selecting two adjacent cows and feeding each a bag of corn, which decreases both their hunger levels by one. The goal is to make all cows have the same non-negative hunger level using the minimum number of bags, or determine if it's impossible.

## Input Format

- First line: T (number of test cases, 1 ≤ T ≤ 100)
- For each test case:
  - Line 1: N (number of cows)
  - Line 2: h₁, h₂, ..., hₙ (hunger levels, where 0 ≤ hᵢ ≤ 10⁹)
- Sum of N across all test cases ≤ 10⁵

## Output Format

T lines, each containing the minimum number of bags needed or -1 if impossible.

## Sample Input

```
5
3
8 10 5
6
4 6 4 4 6 4
3
0 1 0
2
1 2
3
10 9 9
```

## Sample Output

```
14
16
-1
-1
-1
```
