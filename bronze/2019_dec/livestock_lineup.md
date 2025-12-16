# USACO 2019 December Contest, Bronze: Problem 3 - Livestock Lineup

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=965)

## Problem Description

Farmer John needs to milk his 8 dairy cows (Bessie, Buttercup, Belinda, Beatrice, Bella, Blue, Betsy, and Sue) in an order that satisfies N constraints (1 ≤ N ≤ 7). Each constraint specifies that two cows must be milked adjacent to each other. The task is to find a valid ordering that is alphabetically earliest—prioritizing the first cow alphabetically, then the second cow, and so on.

## Input Format

- First line: integer N (number of constraints)
- Next N lines: constraints in the form "X must be milked beside Y"

## Output Format

Eight lines, each containing one cow name, representing a valid milking order that satisfies all constraints and is alphabetically first.

## Sample Input

```
3
Buttercup must be milked beside Bella
Blue must be milked beside Bella
Sue must be milked beside Beatrice
```

## Sample Output

```
Beatrice
Sue
Belinda
Bessie
Betsy
Blue
Bella
Buttercup
```
