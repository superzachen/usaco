# USACO 2024 January Contest, Bronze: Problem 1 - Majority Opinion

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=1371)

## Problem Description

Farmer John needs to determine which types of hay can become universally liked by all N cows through focus groups. Each cow initially prefers exactly one hay type (1 to N).

A focus group involves selecting a contiguous range of cows. If a single hay type is preferred by more than half the cows in that range, all cows in the group switch to that preference. Otherwise, no change occurs.

The goal is to identify all possible hay types that could eventually be liked by all cows after running any number of focus groups.

## Input Format

- First line: integer T (number of test cases, 1 ≤ T ≤ 10)
- For each test case:
  - Line 1: integer N (2 ≤ N ≤ 10⁵)
  - Line 2: N integers representing each cow's hay preference

The sum of N across all test cases does not exceed 2×10⁵.

## Output Format

For each test case, output either:
- All possible hay types (in increasing order, space-separated), or
- "-1" if no universal preference is achievable

## Sample Input

```
5
5
1 2 2 2 3
6
1 2 3 1 2 3
6
1 1 1 2 2 2
3
3 2 3
2
2 1
```

## Sample Output

```
2
-1
1 2
3
-1
```
