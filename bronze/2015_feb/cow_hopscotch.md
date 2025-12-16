# USACO 2015 February Contest, Bronze: Problem 3 - Cow Hopscotch

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=528)

## Problem Description

Cows navigate an R by C grid (2 ≤ R ≤ 15, 2 ≤ C ≤ 15) where each square is colored red or blue. Starting from the top-left corner, they must reach the bottom-right corner through valid jumps. A jump is valid when:

1. The destination square has a different color than the current square
2. The destination is at least one row below the current position
3. The destination is at least one column to the right of the current position

The task is to count the total number of distinct valid jump sequences from start to finish.

## Input Format

- First line: two integers R and C
- Next R lines: C characters each, where each character is 'R' (red) or 'B' (blue)

## Output Format

A single integer representing the number of different valid paths from top-left to bottom-right.

## Sample Input

```
4 4
RRRR
RRBR
RBBR
RRRR
```

## Sample Output

```
3
```
