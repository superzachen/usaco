# USACO 2024 February Contest, Bronze: Problem 3 - Maximizing Productivity

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=1397)

## Problem Description

Farmer John operates N farms, each closing at time cᵢ. Bessie wakes at time S and visits farm i at time tᵢ + S. She can only visit a farm if she arrives strictly before it closes. Given Q queries with values S and V, determine if Bessie can visit at least V farms when waking at time S.

## Input Format

- Line 1: Two integers N and Q
- Line 2: N integers representing c₁, c₂, ..., cₙ (farm closing times, 1 ≤ cᵢ ≤ 10^6)
- Line 3: N integers representing t₁, t₂, ..., tₙ (visit times, 1 ≤ tᵢ ≤ 10^6)
- Next Q lines: Each contains two integers V and S (1 ≤ V ≤ N, 1 ≤ S ≤ 10^6)

## Output Format

For each query, output "YES" or "NO" on a new line indicating whether Bessie can visit at least V farms.

## Sample Input

```
5 5
3 5 7 9 12
4 2 3 3 8
1 5
1 6
3 3
4 2
5 1
```

## Sample Output

```
YES
NO
YES
YES
NO
```

## Explanation

- Query 1 (V=1, S=5): Visit times become [9, 7, 8, 8, 13]. Only farm 4 visits before closing (8 < 9). Answer: YES
- Query 2 (V=1, S=6): All visits occur after closing times. Answer: NO
- Query 3 (V=3, S=3): Farms 3, 4, 5 can be visited on time. Answer: YES
- Query 4 (V=4, S=2): Four farms can be visited on time. Answer: YES
- Query 5 (V=5, S=1): Cannot visit all five farms on time. Answer: NO
