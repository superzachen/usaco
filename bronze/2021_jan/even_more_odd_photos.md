# USACO 2021 January Contest, Bronze: Problem 2 - Even More Odd Photos

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=1084)

## Problem Description

Farmer John needs to photograph N cows (2 ≤ N ≤ 1000), each with a breed ID (1-100). He wants to partition all cows into disjoint groups and arrange them so that the first group's breed ID sum is even, the second group's sum is odd, and so on, alternating. The goal is to maximize the number of groups.

## Input Format

- Line 1: Integer N (number of cows)
- Line 2: N space-separated integers representing breed IDs

## Output Format

A single integer: the maximum possible number of groups

## Sample Input 1

```
7
1 3 5 7 9 11 13
```

## Sample Output 1

```
3
```

**Explanation:** One valid grouping: {1,3} (sum=4, even), {5,7,9} (sum=21, odd), {11,13} (sum=24, even).

## Sample Input 2

```
7
11 2 17 13 1 15 3
```

## Sample Output 2

```
5
```

**Explanation:** One valid grouping: {2} (even), {11} (odd), {13,1} (even), {15} (odd), {17,3} (even).
