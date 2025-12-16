# USACO 2015 US Open Contest, Bronze: Problem 3 - Trapped in the Haybales

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=547)

## Problem Description

Farmer John has placed N hay bales at various positions along a road. Bessie the cow is grazing and may be trapped between them. Each bale has a size and position. Bessie can move freely but cannot cross through a bale's position. However, if she runs in one direction for D units, she can break through any bale with size strictly less than D, potentially opening paths to other bales. The goal is to determine the total area of road positions from which Bessie cannot escape to either end.

## Input Format

- First line: integer N (1 ≤ N ≤ 4000)
- Next N lines: two integers each representing a bale's size and position (both in range 1 to 10^9)

## Output Format

A single integer representing the total area of the road from which Bessie cannot escape.

## Sample Input

```
5
8 1
1 4
8 8
7 15
4 20
```

## Sample Output

```
14
```

## Notes

- The example indicates that if Bessie cannot escape from positions between certain bales, that distance contributes to the trapped area.
- Bales can be eliminated through speed-based breakthrough, creating cascading opportunities.
