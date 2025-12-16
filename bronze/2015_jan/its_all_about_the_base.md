# USACO 2015 January Contest, Bronze: Problem 3 - It's All About the Base

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=509)

## Problem Description

Bessie has learned about number bases and written a number N in two different bases X and Y (both between 10 and 15,000). In both cases, the representation consists of exactly 3 digits, each ranging from 1 to 9. She has forgotten N, X, and Y but remembers the two 3-digit sequences. You must determine the bases used.

Key constraint: A program that searches exhaustively over every possible value of X and Y (nearly 15,000^2 possibilities!) will not run within the time limit, requiring an optimized approach rather than brute force.

## Input Format

- First line: integer K (number of test cases)
- Following K lines: each contains two 3-digit numbers representing N in bases X and Y respectively

## Output Format

For each test case, output X and Y separated by a space on a single line.

## Sample Input

```
1
419 792
```

## Sample Output

```
47 35
```

## Explanation

The number 8892 in base 10 equals 419 when written in base 47 and 792 when written in base 35. The solution must efficiently find such base pairs without exhaustive searching.
