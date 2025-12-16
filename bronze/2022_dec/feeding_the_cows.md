# USACO 2022 December Contest, Bronze: Problem 2 - Feeding the Cows

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=1252)

## Problem Description

Farmer John manages N cows (1 ≤ N ≤ 10⁵) of two breeds: Guernsey (G) or Holstein (H), positioned along a line from 1 to N. To feed them, FJ plants grass patches at select positions. Each patch must be designated for either Guernseys or Holsteins exclusively. Each cow can travel a maximum of K positions to reach an appropriate patch. The task is to determine the minimum number of patches needed and provide a valid configuration.

## Input Format

- First line: T (number of test cases, 1 ≤ T ≤ 10)
- For each test case:
  - Line 1: N and K
  - Line 2: String of length N with characters 'G' (Guernsey) or 'H' (Holstein)

## Output Format

For each test case, output two lines:
- Line 1: Minimum number of patches required
- Line 2: String of length N where each position is '.', 'G', or 'H'

## Sample Input

```
6
5 0
GHHGG
5 1
GHHGG
5 2
GHHGG
5 3
GHHGG
5 4
GHHGG
2 1
GH
```

## Sample Output

```
5
GHHGG
3
.GH.G
2
..GH.
2
...GH
2
...HG
2
HG
```
