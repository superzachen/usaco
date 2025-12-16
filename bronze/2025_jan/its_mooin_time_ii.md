# USACO 2025 January Contest, Bronze: Problem 2 - It's Mooin' Time II

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=1468)

## Problem Description

Farmer John wants to explain his favorite USACO contest to Elsie by describing a concept called a "moo." Given an array of N integers (1 ≤ N ≤ 10⁶, 1 ≤ aᵢ ≤ N):

A "moo" is defined as an array of three integers where the second and third integers are equal to each other, but the first integer differs from them. A moo occurs in the contest if you can remove integers from the array until only the moo remains.

The task is to count the number of distinct moos that occur in the contest. Two moos are distinct if they don't consist of the same integers in the same order.

## Input Format

- Line 1: Integer N
- Line 2: N space-separated integers a₁, a₂, ..., aₙ

## Output Format

Output a single integer representing the number of distinct moos.

**Note:** This problem may require 64-bit integer data types due to large values involved.

## Sample Input

```
6
1 2 3 4 4 4
```

## Sample Output

```
3
```

## Explanation

The three distinct moos are: [1, 4, 4], [2, 4, 4], and [3, 4, 4].
