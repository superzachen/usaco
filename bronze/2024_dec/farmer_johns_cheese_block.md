# USACO 2024 December Contest, Bronze: Problem 2 - Farmer John's Cheese Block

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=1444)

## Problem Description

Farmer John possesses a cubic block of cheese spanning from coordinates (0,0,0) to (N, N, N), where 2 ≤ N ≤ 1000. Through Q operations (1 ≤ Q ≤ 2×10⁵), he carves out unit cubes at specified locations. After each removal, the task is to count how many valid placements exist for a 1×1×N brick within the remaining cheese such that:
- The brick doesn't overlap any remaining cheese
- All brick vertices have integer coordinates within [0,N]
- The brick can be rotated in any direction

## Input Format

The first line contains N and Q. The following Q lines each contain three integers x, y, and z representing the coordinates of unit cubes to be carved out.

## Output Format

After each update operation, output a single integer representing the number of valid brick configurations.

## Sample Input

```
2 5
0 0 0
1 1 1
0 1 0
1 0 0
1 1 0
```

## Sample Output

```
0
0
1
2
5
```
