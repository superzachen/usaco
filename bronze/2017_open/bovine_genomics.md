# USACO 2017 US Open Contest, Bronze: Problem 2 - Bovine Genomics

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=736)

## Problem Description

Farmer John has N cows with spots and N cows without spots. He believes spots are caused by mutations at a single genome location. Each cow's genome is a string of length M using characters A, C, G, and T.

The task is to find positions in the genome that can perfectly predict spottiness by examining that position alone. A position qualifies if all spotted cows share one set of characters at that position while all plain cows share a different, non-overlapping set.

## Input Format

First line contains N and M (both ≤ 100). The next N lines contain genomes of spotted cows (M characters each). The final N lines contain genomes of plain cows (M characters each).

## Output Format

Output a single integer (0 to M) representing the count of positions that could individually explain spottiness.

## Sample Input

```
3 8
AATCCCAT
GATTGCAA
GGTCGCAA
ACTCCCAG
ACTCGCAT
ACTTCCAT
```

## Sample Output

```
1
```
