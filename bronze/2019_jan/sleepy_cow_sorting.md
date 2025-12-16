# USACO 2019 January Contest, Bronze: Problem 2 - Sleepy Cow Sorting

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=892)

## Problem Description

Farmer John needs to sort N cows (1 ≤ N ≤ 100) standing in a line. The cows start in order p₁, p₂, ..., pₙ and must be rearranged to order 1, 2, 3, ..., N.

Only the cow directly facing Farmer John (initially at the front) can receive instructions. In each time step, that cow can move k paces down the line (1 ≤ k ≤ N-1). The k cows she passes move forward to make room for her insertion after them. The objective is to find the minimum number of time steps needed to sort the cows optimally.

## Input Format

- Line 1: Integer N
- Line 2: N space-separated integers representing the initial cow order

## Output Format

A single integer representing the minimum number of time steps needed to achieve sorted order.

## Sample Input

```
4
1 2 4 3
```

## Sample Output

```
3
```
