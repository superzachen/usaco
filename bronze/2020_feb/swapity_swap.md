# USACO 2020 February Contest, Bronze: Problem 3 - Swapity Swap

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=1013)

## Problem Description

Farmer John has N cows (1 ≤ N ≤ 100) standing in a line, labeled 1 through N from left to right. The cows perform a two-step exercise routine exactly K times (1 ≤ K ≤ 10⁹):

1. "The sequence of cows currently in positions A₁ ... A₂ from the left reverse their order"
2. "Then, the sequence of cows currently in positions B₁ ... B₂ from the left reverse their order"

Output the final arrangement after all K iterations.

## Input Format

- Line 1: N and K
- Line 2: A₁ and A₂ (1 ≤ A₁ < A₂ ≤ N)
- Line 3: B₁ and B₂ (1 ≤ B₁ < B₂ ≤ N)

## Output Format

N lines, each containing the label of the cow at that position after all operations.

## Sample Input

```
7 2
2 5
3 7
```

## Sample Output

```
1
2
4
3
5
7
6
```

## Sample Explanation

Starting with [1,2,3,4,5,6,7], after the first complete iteration the order becomes [1,5,7,6,2,3,4]. Repeating this process twice yields the sample output.
