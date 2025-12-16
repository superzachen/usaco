# USACO 2021 December Contest, Bronze: Problem 2 - Air Cownditioning

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=1156)

## Problem Description

Farmer John has N cows in a barn, each in a separate stall. Each cow i has a preferred temperature pᵢ, and the current temperature in stall i is tᵢ. The farmer can issue commands to adjust temperatures in consecutive ranges of stalls by 1 unit (either up or down). The goal is to find the minimum number of commands needed to set each stall to its cow's preferred temperature.

## Input Format

- Line 1: Integer N (number of stalls)
- Line 2: N non-negative integers representing preferred temperatures p₁ ... pₙ
- Line 3: N non-negative integers representing current temperatures t₁ ... tₙ

## Output Format

A single integer representing the minimum number of commands required.

## Sample Input

```
5
1 5 3 3 4
1 2 2 2 1
```

## Sample Output

```
5
```

## Sample Explanation

One optimal sequence of 5 commands transforms the temperatures as follows:
- Initial: `1 2 2 2 1`
- After 3 increases to stalls 2-5: `1 5 5 5 4`
- After 2 decreases to stalls 3-4: `1 5 3 3 4`
