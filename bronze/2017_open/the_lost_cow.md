# USACO 2017 US Open Contest, Bronze: Problem 1 - The Lost Cow

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=735)

## Problem Description

Farmer John must locate his lost cow Bessie on a linear path. John is at position x and Bessie is at unknown position y. Rather than walking directly (distance |x-y|), John must search using a zig-zag pattern: moving to x+1, then x-2, then x+4, and so on, alternating direction while doubling distance each time. This strategy guarantees finding Bessie within 9 times the direct distance. Given John's position and Bessie's location, calculate the total distance traveled.

## Input Format

A single line containing two distinct space-separated integers x and y, each in range 0 to 1000.

## Output Format

One line with the total distance Farmer John travels to reach Bessie.

## Sample Input

```
3 6
```

## Sample Output

```
9
```
