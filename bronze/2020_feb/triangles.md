# USACO 2020 February Contest, Bronze: Problem 1 - Triangles

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=1011)

## Problem Description

Farmer John needs to create a triangular pasture by selecting three fence posts from N available posts as vertices. The constraint is that one side must be parallel to the x-axis and another side must be parallel to the y-axis. The goal is to find the maximum possible area of such a triangle.

## Input Format

The first line contains integer N (where 3 ≤ N ≤ 100). Each subsequent line contains two integers representing the coordinates (Xᵢ, Yᵢ) of a fence post, with coordinates in the range -10⁴ to 10⁴.

## Output Format

Output twice the maximum area of the valid triangle (as an integer, since the actual area may not be).

## Sample Input

```
4
0 0
0 1
1 0
1 2
```

## Sample Output

```
2
```

## Sample Explanation

The posts at (0,0), (1,0), and (1,2) form a triangle with area 1, giving an output of 2×1=2. Another valid triangle in the input has area 0.5.
