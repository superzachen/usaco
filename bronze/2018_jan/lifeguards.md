# USACO 2018 January Contest, Bronze: Problem 2 - Lifeguards

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=784)

## Problem Description

Farmer John operates a swimming pool open from time t=0 to t=1000. He employs N cows as lifeguards, each working a shift covering a contiguous time interval. A shift from time a to time b covers (b-a) units of time. Farmer John must fire exactly one lifeguard due to budget constraints. The goal is to find the maximum time coverage achievable with the remaining (N-1) lifeguards, where coverage means at least one lifeguard is present during that interval.

## Input Format

- First line: integer N (1 ≤ N ≤ 100)
- Next N lines: two integers per line representing a lifeguard's shift start and end times (range 0-1000)
- All endpoints are distinct

## Output Format

A single integer representing the maximum time coverage possible after removing one lifeguard.

## Sample Input

```
3
5 9
1 4
3 7
```

## Sample Output

```
7
```
