# USACO 2019 February Contest, Bronze: Problem 2 - The Great Revegetation

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=916)

## Problem Description

Farmer John has N pastures that need to be revegetated with one of four grass seed types. He has M cows, each with two favorite pastures. The goal is to assign a grass type (1-4) to each pasture such that each cow's two favorite pastures have different grass types. No pasture is favored by more than 3 cows.

## Input Format

- First line: Two integers N (2 ≤ N ≤ 100) and M (1 ≤ M ≤ 150)
- Next M lines: Two integers each in range 1 to N, representing a cow's two favorite pastures

File: `revegetate.in`

## Output Format

An N-digit number where each digit is in range 1-4, representing the grass type for each pasture in order. If multiple solutions exist, output the lexicographically smallest one.

File: `revegetate.out`

## Sample Input

```
5 6
4 1
4 2
4 3
2 5
1 2
1 5
```

## Sample Output

```
12133
```
