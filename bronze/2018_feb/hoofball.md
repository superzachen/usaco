# USACO 2018 February Contest, Bronze: Problem 2 - Hoofball

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=808)

## Problem Description

Farmer John is training N cows (numbered 1 to N, where 1 ≤ N ≤ 100) for a hoofball tournament. The cows stand along a line at positions xᵢ units from a barn (1 ≤ xᵢ ≤ 1000), each at a distinct location.

When a cow receives a ball, she passes it to the nearest cow. If multiple cows are equidistant, she passes to the leftmost one. Farmer John needs to distribute balls initially to ensure every cow handles the ball at least once. The task is to find the minimum number of initial balls needed.

## Input Format

- Line 1: Integer N (number of cows)
- Line 2: N space-separated integers representing positions xᵢ

## Output Format

A single integer representing the minimum number of balls Farmer John must initially distribute.

## Sample Input

```
5
7 1 3 11 4
```

## Sample Output

```
2
```

## Explanation

Distributing balls to cows at positions 1 and 11 ensures all cows eventually receive a ball through passing, with oscillations occurring between certain cows.
