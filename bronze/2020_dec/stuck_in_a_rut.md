# USACO 2020 December Contest, Bronze: Problem 3 - Stuck in a Rut

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=1061)

## Problem Description

Farmer John's farm is represented as an infinite 2D grid. There are N cows (1 ≤ N ≤ 50), each starting in a different cell facing either north or east. Each hour, a cow either stops (if grass in its cell was eaten) or eats the grass and moves forward in its facing direction. When cows move onto the same grassy cell simultaneously, they share it and continue in their respective directions. The task is to determine how much grass each cow eats (some eat infinitely).

## Input Format

The first line contains N. Each of the next N lines contains a direction character (N or E) and two nonnegative integers x and y (0 ≤ x, y ≤ 10⁹). All x-coordinates are distinct, as are all y-coordinates. North movement: (x, y) → (x, y+1). East movement: (x, y) → (x+1, y).

## Output Format

Print N lines. Line i should show the grass count for cow i, or "Infinity" if the cow never stops.

## Sample Input

```
6
E 3 5
N 5 3
E 4 6
E 10 4
N 11 2
N 8 1
```

## Sample Output

```
5
3
Infinity
Infinity
2
5
```
