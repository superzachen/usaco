# USACO 2016 January Contest, Bronze: Problem 3 - Mowing the Field

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=593)

## Problem Description

Farmer John starts mowing a 2D grid at time t=0, beginning in one cell. He follows a sequence of N movement commands, each specifying a direction and number of steps. As he moves, he mows grass in each cell he visits.

The key constraint: grass cut at time t regrows at time t+x. FJ never encounters already-cut grass, meaning each cell revisit occurs at least x time units after the previous visit.

The task is to find the maximum value of x that satisfies this constraint, or -1 if no cell is visited twice.

## Input Format

First line contains N (1 ≤ N ≤ 100). The next N lines each contain a direction letter (N/E/S/W) and number of steps S (1 ≤ S ≤ 10).

## Output Format

Output the maximum value of x such that grass never appears cut when FJ visits it. Output -1 if FJ never revisits any cell.

## Sample Input

```
6
N 10
E 2
S 3
W 4
S 5
E 8
```

## Sample Output

```
10
```

## Explanation

FJ revisits a cell at time 17 that he first visited at time 7, constraining x ≤ 10. He also revisits a cell at time 26 from time 2, constraining x ≤ 24. The tighter constraint (x ≤ 10) determines the answer.
