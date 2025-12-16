# USACO 2018 January Contest, Bronze: Problem 1 - Blocked Billboard II

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=783)

## Problem Description

Bessie needs to cover an offensive lawnmower billboard with a rectangular tarp. A cow feed billboard is positioned in front of the lawnmower billboard and may partially obscure it. Bessie must determine the minimum tarp area needed to completely hide the remaining visible portion of the lawnmower billboard.

Key constraints: The tarp must have sides parallel to the billboards (no tilting allowed).

## Input Format

The first line contains four space-separated integers: `x₁ y₁ x₂ y₂`, representing the lower-left and upper-right corners of the lawnmower billboard.

The second line contains four integers specifying the lower-left and upper-right corners of the cow feed billboard.

All coordinates range from -1000 to +1000.

## Output Format

Output the minimum area of the rectangular tarp needed to completely obscure the lawnmower billboard.

## Sample Input

```
2 1 7 4
5 -1 10 3
```

## Sample Output

```
15
```

## Explanation

The cow feed billboard partially obscures the lawnmower billboard's lower-right corner, but the entire lawnmower billboard area (15 square units) still requires coverage.
