# USACO 2015 January Contest, Bronze: Problem 1 - Cow Routing

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=507)

## Problem Description

Bessie seeks the most economical way to travel between two cities using Air Bovinia's airline system. The airline operates N planes, each following a specific route through multiple cities. When using a route, Bessie can board at any city along it and exit at any subsequent city. The cost applies regardless of how many cities she traverses on that route. The constraint is that she wants to use only a single route.

## Input Format

- Line 1: Three integers A, B, and N (where 1 ≤ N ≤ 500)
  - A: starting city
  - B: destination city
  - N: number of routes
- Next 2N lines: For each route:
  - Line 1: Cost (1-1000) and number of cities
  - Line 2: List of cities in order (integers 1-10,000)

## Output Format

Output the minimum cost to travel from city A to B using a single route, or -1 if impossible.

## Sample Input

```
1 2 3
3 3
3 2 1
4 4
2 1 4 3
8 5
1 7 8 2
```

## Sample Output

```
8
```

## Solution Notes

Although a two-route solution exists cheaper (route 2 from city 1→3, then route 1 from city 3→2), the single-route constraint requires using route 3 at cost 8.
