# USACO 2019 US Open Contest, Bronze: Problem 3 - Cow Evolution

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=941)

## Problem Description

In the year 3019, cows have evolved diverse features through a tree-based evolutionary process. Starting from an ancestral cow with no special features, evolution occurs either through universal feature adoption (all descendants gain a trait) or divergent splits (some descendants gain a trait, others don't).

The key constraint: "a tree would not be proper if spots evolved into being in two separate branches." Each feature must originate on exactly one edge of the evolutionary tree to be considered "proper."

Given descriptions of final cow sub-populations in 3019, determine whether they can be explained by a proper evolutionary tree.

## Input Format

- First line: number of sub-populations, N (2 ≤ N ≤ 25)
- Next N lines: each describes a sub-population with integer K (0 ≤ K ≤ 25) followed by K characteristics (lowercase strings, max 20 characters each)
- No two sub-populations share identical characteristic sets

## Output Format

Output "yes" if a proper evolutionary tree can explain the sub-populations, otherwise output "no".

## Sample Input

```
4
2 spots firebreathing
0
1 flying
2 telepathic flying
```

## Sample Output

```
yes
```
