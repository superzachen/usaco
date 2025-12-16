# USACO 2015 January Contest, Bronze: Problem 2 - Cow Routing II

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=508)

## Problem Description

Bessie seeks the cheapest way to travel from city A to city B using Air Bovinia's routes. Each plane operates on a specific route through multiple cities. Bessie can board at any city along a route and disembark at any later city. Each route costs a fixed amount regardless of distance traveled, and can only be used once. The constraint here is that Bessie wants to use at most two routes to reach her destination.

## Input Format

- Line 1: Three integers A, B, and N (where 1 ≤ N ≤ 500)
  - A: starting city
  - B: destination city
  - N: number of available routes
- Lines 2 through 2N+1: Each route described in two lines
  - First line: cost (1-1000) and city count (1-500)
  - Second line: space-separated list of cities in route order

## Output Format

Output the minimum cost to travel from A to B using at most two routes, or -1 if no solution exists.

## Sample Input

```
1 2 3
3 3
3 2 1
4 4
1 4 3 8
5 4
1 7 8 2
```

## Sample Output

```
7
```

## Explanation

The optimal solution uses route 2 (cost 4) from city 1 to city 3, then route 1 (cost 3) from city 3 to city 2, totaling 7.
