# USACO 2024 December Contest, Bronze: Problem 1 - Roundabout Rounding

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=1443)

## Problem Description

Bessie performs standard rounding to powers of 10: to round a number `a` to the nearest `10^b`, she locates the b-th digit from the right (call it `x`). If `x ≥ 5`, she adds `10^b` to `a`. Then she sets all digits at and to the right of position b to zero.

Elsie proposes "chain rounding": round to `10^1`, then to `10^2`, continuing until `10^b`.

The task is to count integers from 2 to N where direct rounding to `10^P` differs from chain rounding to `10^P`, where P is the smallest integer such that `10^P ≥ x`.

## Input Format

- First line: integer T (1 ≤ T ≤ 10^5) indicating test cases
- Each test case: single integer N (1 ≤ N ≤ 10^9)
- All N values within the same input are distinct

## Output Format

For each test case, output one integer representing the count of integers from 2 to N where the two rounding methods produce different results.

## Sample Input

```
4
1
100
4567
3366
```

## Sample Output

```
0
5
183
60
```

## Explanation

For N=100, the number 48 qualifies because chain rounding gives 100 (48→50→100) while direct rounding to 10^2 gives 0.
