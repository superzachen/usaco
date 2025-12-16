# USACO 2019 US Open Contest, Bronze: Problem 1 - Bucket Brigade

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=939)

## Problem Description

A fire has broken out on a farm, and cows need to form a "bucket brigade" to extinguish it. The farm is represented as a 10×10 grid containing:
- 'B': the barn (on fire)
- 'L': a lake (water source)
- 'R': a large rock (impassable)
- '.': empty squares where cows can be placed

Cows must be positioned along a path between the lake and barn so buckets can be passed between adjacent cows (in cardinal directions only). A cow adjacent to the lake can extract water, and a cow adjacent to the barn can throw water on it.

The task is to find the minimum number of cows needed to form a viable bucket brigade. Cows cannot occupy the rock square.

## Input Format

The input file contains 10 rows, each with 10 characters describing the farm layout.

## Output Format

A single integer representing the minimum number of cows needed.

## Sample Input

```
..........
..........
..........
..B.......
..........
.....R....
..........
..........
.....L....
..........
```

## Sample Output

```
7
```
