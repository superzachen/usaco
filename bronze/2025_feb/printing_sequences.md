# USACO 2025 February Contest, Bronze: Problem 3 - Printing Sequences

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=1493)

## Problem Description

Bessie is learning a simple programming language with two statement types:
- "PRINT c" appends integer c to output
- "REP o" followed by a program and "END" executes the inner program o times

The challenge: produce a given sequence of N positive integers (each ≤ K) using at most K "PRINT" statements. REP statements are unlimited.

Example program structure:
```
REP 3
    PRINT 1
    REP 2
        PRINT 2
    END
END
```
This outputs [1,2,2,1,2,2,1,2,2].

## Input Format

- First line: T (number of test cases)
- For each test case:
  - Line 1: N and K (sequence length and max PRINT statements allowed)
  - Line 2: N space-separated positive integers (the target sequence)

## Output Format

For each test case, output "YES" or "NO" indicating whether the sequence is achievable.

## Sample Input

```
2
1 1
1
4 1
1 1 1 1
```

## Sample Output

```
YES
YES
```

## Extended Sample

```
Input:
11
4 2
1 2 2 2
4 2
1 1 2 1
4 2
1 1 2 2
6 2
1 1 2 2 1 1
10 2
1 1 1 2 2 1 1 1 2 2
8 3
3 3 1 2 2 1 2 2
9 3
1 1 2 2 2 3 3 3 3
16 3
2 2 3 2 2 3 1 1 2 2 3 2 2 3 1 1
24 3
1 1 2 2 3 3 3 2 2 3 3 3 1 1 2 2 3 3 3 2 2 3 3 3
9 3
1 2 2 1 3 3 1 2 2
6 3
1 2 1 2 2 3

Output:
YES
NO
YES
NO
YES
YES
YES
YES
YES
NO
NO
```
