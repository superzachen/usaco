# USACO 2023 December Contest, Bronze: Problem 2 - Cowntact Tracing 2

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=1348)

## Problem Description

Farmer John has N cows arranged in a line. Some cows start infected, and each night, infected cows spread sickness to adjacent cows (left and right). Once infected, cows remain infected. Given the final state after an unknown number of nights, determine the minimum number of cows that could have been initially infected.

## Input Format

- Line 1: Integer N (the number of cows, where 1 ≤ N ≤ 3×10⁵)
- Line 2: An N-character bitstring of 1s and 0s, where 1 represents an infected cow and 0 represents an uninfected cow

## Output Format

A single integer representing the minimum number of cows that could have started with the sickness.

## Sample Input 1

```
5
11111
```

## Sample Output 1

```
1
```

Starting with only the middle cow infected (00100), the infection spreads outward until all cows are infected.

## Sample Input 2

```
6
011101
```

## Sample Output 2

```
4
```

The isolated 0 in the middle cannot be reached by spreading from adjacent infected cows, so all four 1s must have been initially infected.
