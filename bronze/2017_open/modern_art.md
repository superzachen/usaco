# USACO 2017 US Open Contest, Bronze: Problem 3 - Modern Art

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=737)

## Problem Description

Picowso is a bovine painter who creates art through a specific process. Starting with an N×N canvas filled with zeros, she paints 9 rectangles using colors numbered 1-9. Each rectangle has sides parallel to the canvas edges and can range from a single cell to the entire canvas. Colors are applied sequentially, with later paintings potentially obscuring earlier ones. All colors 1-9 are used exactly once, though some may be completely hidden in the final result.

Given the final canvas state, determine how many visible colors could have been painted first.

## Input Format

The first line contains N, the canvas size (1 ≤ N ≤ 10). The next N lines each contain N numbers ranging from 0-9, representing the final canvas. The input is guaranteed to represent a valid painting sequence as described.

## Output Format

Output a single integer: the count of visible colors that could have been the first color painted.

## Sample Input

```
4
2230
2737
2777
0000
```

## Sample Output

```
1
```

## Sample Explanation

Only color 2 could have been painted first, as "color 3 clearly had to have been painted after color 7, and color 7 clearly had to have been painted after color 2."
