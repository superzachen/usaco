# USACO 2019 January Contest, Bronze: Problem 1 - Shell Game

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=891)

## Problem Description

Bessie places a pebble under one of three inverted shells and performs a series of swaps while Elsie makes guesses about the pebble's location after each swap. Elsie scores one point for each correct guess. The initial pebble location is unknown, so the task is to determine the maximum possible score across all possible starting positions.

## Input Format

The first line contains an integer N (1 ≤ N ≤ 100) representing the number of swaps. Each of the next N lines contains three integers a, b, and g, where:
- Shells a and b are swapped
- Elsie guesses shell g after the swap
- All values are 1, 2, or 3, with a ≠ b

## Output Format

Output the maximum number of points Elsie could have earned.

## Sample Input

```
3
1 2 1
3 2 1
1 3 1
```

## Sample Output

```
2
```

## Explanation

By testing each possible starting position: if the pebble begins under shell 1, Elsie scores 1 point (correct on the final guess). If starting under shell 2, she scores 2 points (correct on the first two guesses). If starting under shell 3, she scores 0 points. The maximum is 2 points.
