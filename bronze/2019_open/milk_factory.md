# USACO 2019 US Open Contest, Bronze: Problem 2 - Milk Factory

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=940)

## Problem Description

Farmer John's milk factory consists of N processing stations connected by N-1 walkways forming a tree structure. Each walkway has a one-directional conveyor belt. The task is to determine if there exists a station that can be reached from all other stations by following the conveyor belt directions.

## Input Format

- First line: Integer N (1 ≤ N ≤ 100), the number of processing stations
- Next N-1 lines: Two space-separated integers `a_i` and `b_i` representing a conveyor belt from station `a_i` to station `b_i`

## Output Format

Output the minimal station number `i` from which all other stations can reach it by following conveyor directions. If no such station exists, output `-1`.

## Sample Input

```
3
1 2
3 2
```

## Sample Output

```
2
```

## Explanation

In the sample, station 2 can be reached from both station 1 (via the 1→2 belt) and station 3 (via the 3→2 belt), making it a valid destination.
