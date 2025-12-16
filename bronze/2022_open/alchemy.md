# USACO 2022 US Open Contest, Bronze: Problem 3 - Alchemy

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=1229)

## Problem Description

Bessie is learning metal transformation through alchemy. She possesses various quantities of different metals and knows several recipes for combining metals. Each recipe allows her to combine one unit each of several constituent metals to produce one unit of a higher-numbered metal. At most one recipe exists per metal type.

The goal is to determine the maximum number of units of metal N that can be obtained through a series of transformations.

## Input Format

- Line 1: Integer N (number of metal types)
- Line 2: N integers representing initial quantities of each metal
- Line 3: Integer K (number of recipes)
- Next K lines: Each starts with integers L and M, followed by M integers representing constituent metals needed to create one unit of metal L

## Output Format

Maximum number of units of metal N achievable after zero or more transformations.

## Sample Input

```
5
2 0 0 1 0
3
5 2 3 4
2 1 1
3 1 2
```

## Sample Output

```
1
```

## Sample Explanation

The optimal transformation sequence:
1. Convert one unit of metal 1 → metal 2
2. Convert one unit of metal 2 → metal 3
3. Convert one unit of metal 3 + one unit of metal 4 → metal 5

Result: 1 unit of metal 5 (plus 1 unit of metal 1 remaining)
