# USACO 2021 January Contest, Bronze: Problem 3 - Just Stalling

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=1085)

## Problem Description

Farmer John has N cows with specific heights and a barn containing N stalls, each with maximum height limits. The task is to determine how many distinct arrangements exist where each cow occupies a different stall and respects all height constraints.

## Input Format

- Line 1: Integer N (1 ≤ N ≤ 20)
- Line 2: N space-separated integers representing cow heights (a₁, a₂, ..., aₙ)
- Line 3: N space-separated integers representing stall height limits (b₁, b₂, ..., bₙ)

All heights and limits are in the range [1, 10⁹].

## Output Format

A single integer representing the number of valid arrangements where each cow is placed in a different stall and every height constraint is satisfied. Output may require a 64-bit integer.

## Sample Input

```
4
1 2 3 4
2 4 3 4
```

## Sample Output

```
8
```

## Sample Explanation

The example demonstrates that certain placements are invalid (e.g., cow 3 cannot use stall 1 since its height 3 exceeds the limit of 2). One valid arrangement places cows 1-4 in stalls 1-4 respectively.
