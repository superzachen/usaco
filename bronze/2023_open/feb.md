# USACO 2023 US Open Contest, Bronze: Problem 1 - FEB

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=1323)

## Problem Description

Bessie and Elsie communicate through N text messages represented by string S, where each character is either 'B' (Bessie), 'E' (Elsie), or 'F' (obfuscated by Farmer John). The "excitement level" counts occurrences of "BB" or "EE" substrings. Given that some characters are unknown, determine all possible excitement levels.

## Input Format

- Line 1: Integer N (1 ≤ N ≤ 2×10⁵)
- Line 2: String S of length N containing characters B, E, or F

## Output Format

- Line 1: K (number of distinct possible excitement levels)
- Lines 2 to K+1: Each possible excitement level in increasing order

## Sample Input 1

```
4
BEEF
```

## Sample Output 1

```
2
1
2
```

## Sample Input 2

```
9
FEBFEBFEB
```

## Sample Output 2

```
2
2
3
```

## Sample Input 3

```
10
BFFFFFEBFE
```

## Sample Output 3

```
3
2
4
6
```
