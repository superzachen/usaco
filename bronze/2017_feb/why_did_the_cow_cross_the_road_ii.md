# USACO 2017 February Contest, Bronze: Problem 2 - Why Did the Cow Cross the Road II

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=712)

## Problem Description

Farmer John's farm features a circular road with 26 cows (named A-Z) crossing it daily. Each cow has a distinct entry point and exit point on the circle, creating 52 total crossing points. When scanned clockwise, these points form a 52-character string with each letter appearing exactly twice.

He calls a pair of cows (a,b) a 'crossing' pair if cow a's path from entry to exit must cross cow b's path from entry to exit. The task is to count all crossing pairs.

## Input Format

A single line containing a 52-character string of uppercase letters, where each letter A-Z appears exactly twice.

## Output Format

Print the total number of crossing pairs.

## Sample Input

```
ABCCABDDEEFFGGHHIIJJKKLLMMNNOOPPQQRRSSTTUUVVWWXXYYZZ
```

## Sample Output

```
1
```

The sample demonstrates that only cows A and B form a crossing pair in this configuration.
