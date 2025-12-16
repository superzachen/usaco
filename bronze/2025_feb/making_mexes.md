# USACO 2025 February Contest, Bronze: Problem 2 - Making Mexes

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=1492)

## Problem Description

Given an array of N non-negative integers, you can change any element to any non-negative integer in one operation. The *mex* of an array is "the minimum non-negative integer that it does not contain."

For each value i from 0 to N inclusive, determine the minimum number of operations needed to make the array's mex equal to i.

## Input Format

- First line: N (the array size)
- Second line: N space-separated integers representing the array elements

Constraints: 1 ≤ N ≤ 2×10⁵, 0 ≤ aᵢ ≤ N

## Output Format

N+1 lines, each containing the minimum number of operations required to achieve mex equal to i (for i = 0 to N).

## Sample Input

```
4
2 2 2 0
```

## Sample Output

```
1
0
3
1
2
```

## Explanation

- mex = 0: Change one element to make 0 absent (e.g., change a₄ to 3)
- mex = 1: Already true; array [2,2,2,0] lacks 1
- mex = 2: Requires 3 operations to construct [3,1,1,0]
- mex = 3: Requires 1 operation
- mex = 4: Requires 2 operations
