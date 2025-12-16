# USACO 2015 January Contest, Bronze: Problem 4 - Meeting Time

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=510)

## Problem Description

Bessie and Elsie need to travel from a barn (field 1) to their favorite field (field N), departing simultaneously and arriving at the same time. The farm consists of N fields arranged by elevation, with paths that only go downhill (from lower-numbered to higher-numbered fields). Each person may traverse paths at different speeds.

## Input Format

- First line: N (number of fields, 1 ≤ N ≤ 16) and M (number of paths)
- Following M lines: Four integers A B C D where:
  - A and B are field numbers with A < B
  - C is Bessie's travel time on that path
  - D is Elsie's travel time on that path
  - C and D range from 1 to 1000

## Output Format

A single integer representing the minimum time for both travelers to reach field N simultaneously, or "IMPOSSIBLE" if unreachable or no valid solution exists.

## Sample Input

```
3 3
1 3 1 2
1 2 1 2
2 3 1 2
```

## Sample Output

```
2
```

## Explanation

The solution demonstrates that despite Bessie being twice as fast as Elsie on each path, they can synchronize by taking different routes. Bessie takes path 1→2→3 while Elsie takes path 1→3, both arriving in 2 time units.
