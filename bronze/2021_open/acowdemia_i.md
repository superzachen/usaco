# USACO 2021 US Open Contest, Bronze: Problem 1 - Acowdemia I

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=1131)

## Problem Description

Bessie has published N papers with citation counts. The h-index is defined as "the largest number h such that the researcher has at least h papers each with at least h citations."

Bessie plans to write a survey article citing up to L of her past papers (each paper cited at most once) to increase her h-index. Determine the maximum h-index achievable.

## Input Format

- Line 1: Two integers N and L (1 ≤ N ≤ 10⁵, 0 ≤ L ≤ 10⁵)
- Line 2: N space-separated integers representing citation counts c₁, ..., cₙ (0 ≤ cᵢ ≤ 10⁵)

## Output Format

A single integer: the maximum h-index after the survey.

## Sample Input 1

```
4 0
1 100 2 3
```

## Sample Output 1

```
2
```

**Explanation:** With no citations available (L=0), the h-index of (1,100,2,3) is 2.

## Sample Input 2

```
4 1
1 100 2 3
```

## Sample Output 2

```
3
```

**Explanation:** Citing the third paper yields (1,100,3,3), which has h-index 3.
