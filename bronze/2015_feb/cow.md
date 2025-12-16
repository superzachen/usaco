# USACO 2015 February Contest, Bronze: Problem 2 - COW

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=527)

## Problem Description

Bessie discovers an inscription using only three characters: C, O, and W. She wants to count how many times "COW" appears as a subsequence (not necessarily contiguous) in the text. Characters can be interspersed, and different COW occurrences may share letters.

Examples provided:
- "CWOW" contains COW once
- "CCOW" contains COW twice
- "CCOOWW" contains COW eight times

## Input Format

- Line 1: A single integer N ≤ 10^5
- Line 2: A string of N characters, each being C, O, or W

## Output Format

Output the count of COW subsequences. Use 64-bit integers due to potentially large results.

## Sample Input

```
6
COOWWW
```

## Sample Output

```
6
```
