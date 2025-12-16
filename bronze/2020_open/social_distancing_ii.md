# USACO 2020 US Open Contest, Bronze: Problem 2 - Social Distancing II

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=1036)

## Problem Description

Farmer John has N cows positioned at distinct points along a one-dimensional path. Some cows are infected with COWVID-19. The infection spreads to any cow within radius R units of an infected cow. Given which cows are currently infected, determine the minimum number of cows that were initially infected before the disease spread.

## Input Format

- First line: integer N (1 ≤ N ≤ 1000)
- Next N lines: two integers per line
  - `x`: position of cow (0 ≤ x ≤ 10⁶)
  - `s`: health status (0 = healthy, 1 = sick)
- At least one cow is sick, and all cows that could have become infected have done so

## Output Format

Output the minimum possible number of cows initially infected before disease spread occurred.

## Sample Input

```
6
7 1
1 1
15 1
3 1
10 0
6 1
```

## Sample Output

```
3
```

## Sample Explanation

Since R must be less than 3 (otherwise the healthy cow at position 10 would have been infected from position 7), at least 3 cows must have started infected: one from positions 1-3, one from positions 6-7, and the cow at position 15.
