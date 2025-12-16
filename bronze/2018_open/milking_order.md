# USACO 2018 US Open Contest, Bronze: Problem 2 - Milking Order

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=832)

## Problem Description

Farmer John has N cows with a complex social structure governing their milking order. The structure is based on two constraints:

1. **Social Hierarchy**: Some cows must be milked in a specific relative order based on their social status
2. **Position Requirements**: Some cows must be milked at specific absolute positions

Cow 1 has fallen ill, and the goal is to determine the earliest position in the milking order where cow 1 can be placed while satisfying all constraints.

## Input Format

- **Line 1**: Three integers N, M, and K
  - N: number of cows (2 ≤ N ≤ 100)
  - M: number of cows in the social hierarchy (1 ≤ M < N)
  - K: number of cows with position requirements (1 ≤ K < N)
- **Line 2**: M distinct integers representing the required milking order for hierarchical cows
- **Next K lines**: Two integers per line: cow number (cᵢ) and required position (pᵢ)

## Output Format

Output a single integer representing the earliest position where cow 1 can be milked.

## Sample Input

```
6 3 2
4 5 6
5 3
3 1
```

## Sample Output

```
4
```

## Explanation

Cow 3 must be in position 1, cow 4 before cow 5, and cow 5 in position 3. This forces cow 4 into position 2, leaving position 4 as the earliest slot for cow 1.
