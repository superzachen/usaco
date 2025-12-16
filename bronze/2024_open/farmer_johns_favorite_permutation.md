# USACO 2024 US Open Contest, Bronze: Problem 3 - Farmer John's Favorite Permutation

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=1421)

## Problem Description

Farmer John has a permutation `p` of length `N` (where `2 ≤ N ≤ 10^5`). Farmer Nhoj has disassembled it and provides hints to help reconstruct it.

Nhoj generates hints by repeatedly processing the remaining elements. While elements remain:
- If the first element is greater than the last element, write down the second element and remove the first
- Otherwise, write down the second-to-last element and remove the last

This process generates `N-1` hints: `h₁, h₂, ..., h_{N-1}`.

The goal is to find the lexicographically smallest permutation `p` consistent with the given hints, or output `-1` if impossible.

## Input Format

Each test case contains:
- Line 1: Integer `N`
- Line 2: `N-1` integers representing hints `h₁, h₂, ..., h_{N-1}` (where `1 ≤ hᵢ ≤ N`)

Multiple test cases (1 ≤ T ≤ 10)

## Output Format

For each test case, output either:
- The lexicographically smallest valid permutation as space-separated integers, or
- `-1` if no valid permutation exists

## Sample Input

```
5
2
1
2
2
4
1 1 1
4
2 1 1
4
3 2 1
```

## Sample Output

```
1 2
-1
-1
3 1 2 4
1 2 3 4
```
