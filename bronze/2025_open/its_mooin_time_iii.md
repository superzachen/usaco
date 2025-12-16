# USACO 2025 US Open Contest, Bronze: Problem 3 - It's Mooin' Time III

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=1517)

## Problem Description

Given a string of lowercase letters, find valid triplets that form "moos." A moo is defined as a three-character string where the second and third characters match, but differ from the first character.

For a valid triplet (i, j, k) where i < j < k and s_i s_j s_k forms a moo, the value is calculated as "(j-i)(k-j)", representing twice the area of a triangle formed by bending the string at position j.

Bessie asks Q queries, each specifying a range [l, r]. For each query, find the maximum value among all valid triplets within that range, or return -1 if none exist.

## Input Format

- First line: two integers N and Q (3 ≤ N ≤ 10^5, 1 ≤ Q ≤ 3×10^4)
- Second line: string s of length N containing lowercase alphabetic characters
- Following Q lines: two integers l and r for each query (1 ≤ l ≤ r ≤ N, r-l+1 ≥ 3)

## Output Format

Output the maximum value for each query on a new line, or -1 if no valid triplet exists.

## Sample Input

```
12 5
abcabbacabac
1 12
2 7
4 8
2 5
3 10
```

## Sample Output

```
28
6
1
-1
12
```
