# USACO 2020 January Contest, Bronze: Problem 3 - Race

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=989)

## Problem Description

Bessie runs a race of length K meters (where 1 ≤ K ≤ 10⁹). Starting at 0 m/s, she can adjust her speed each second by increasing it by 1 m/s, keeping it the same, or decreasing it by 1 m/s (but never below 0). She must finish at an integer number of seconds, covering at least K meters, with her final speed being at most X m/s. The goal is to find the minimum time needed for N different values of X.

## Input Format

- First line: two integers K and N
- Next N lines: each contains a single integer X (where 1 ≤ X ≤ 10⁵)

## Output Format

N lines, each containing the minimum time in seconds for the corresponding X value.

## Sample Input

```
10 5
1
2
3
4
5
```

## Sample Output

```
6
5
5
4
4
```

## Sample Explanation

For X = 1: An optimal 6-second strategy accelerates to 2 m/s, maintains that speed, then decelerates to 1 m/s at the finish.

For X = 3: An optimal 5-second strategy accelerates to 3 m/s, then maintains that speed, reaching 12 meters total (exceeding the 10-meter requirement).
