# USACO 2022 December Contest, Bronze: Problem 3 - Reverse Engineering

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=1253)

## Problem Description

Elsie has a program that takes an array of N variables (each 0 or 1) and applies a sequence of if/else if/else statements, each examining at most one input variable and returning 0 or 1. Bessie knows the correct outputs for M different inputs and must determine whether Elsie's claims are consistent with such a program, or if she must be lying.

The key constraint: "no program of the form above is consistent with what Elsie said" if there are contradictions.

## Input Format

- First line: T (number of test cases)
- Each test case: N and M, followed by M lines
- Each data line: a string of N binary digits (input) and one binary digit (expected output)
- Test cases separated by blank lines

## Output Format

For each test case, output either "OK" or "LIE"

## Sample Input

```
4

1 3
0 0
0 0
1 1

2 4
00 0
01 1
10 1
11 1

1 2
0 1
0 0

2 4
00 0
01 1
10 1
11 0
```

## Sample Output

```
OK
OK
LIE
LIE
```
