# USACO 2020 January Contest, Bronze: Problem 2 - Photoshoot

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=988)

## Problem Description

Farmer John needs to reconstruct a permutation of N cows. He originally planned an arrangement and recorded consecutive sums, but the original permutation was lost. Given a sequence of sums where each element represents the sum of adjacent pairs in the original arrangement, you must recover the "lexicographically minimum" permutation that could have produced those sums.

A permutation is lexicographically smaller than another if they match up to some position, then the first has a smaller value at that position.

## Input Format

- Line 1: A single integer N (the number of cows, where 2 ≤ N ≤ 10³)
- Line 2: N-1 space-separated integers representing the sums b₁, b₂, ..., b_{N-1}

## Output Format

A single line containing N space-separated integers representing the permutation a₁, a₂, ..., aₙ

## Sample Input

```
5
4 6 7 6
```

## Sample Output

```
3 1 5 2 4
```

## Explanation

The output produces the given sums: 3+1=4, 1+5=6, 5+2=7, 2+4=6.
