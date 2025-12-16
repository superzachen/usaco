# USACO 2020 US Open Contest, Bronze: Problem 1 - Social Distancing I

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=1035)

## Problem Description

Farmer John's barn contains N stalls in a row, some occupied by cows and some vacant. He wants to maximize D, the minimum distance between any two occupied stalls. Two new cows need to be placed in empty stalls to optimize this distance. Existing cows cannot be moved.

## Input Format

- Line 1: Integer N (the number of stalls)
- Line 2: String of length N containing 0s (empty) and 1s (occupied stalls)
- The string is guaranteed to have at least two 0s

## Output Format

Print the largest possible value of D after optimally placing the two new cows.

## Sample Input

```
14
10001001000010
```

## Sample Output

```
2
```

## Explanation

One optimal placement creates the pattern `10x010010x0010` (where x marks new cow positions), achieving D = 2. No higher value is possible with this configuration.
