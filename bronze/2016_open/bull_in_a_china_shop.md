# USACO 2016 US Open Contest, Bronze: Problem 2 - Bull in a China Shop

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=640)

## Problem Description

Farmer John purchased a delicate glass cow figurine but a bull broke it into two pieces that became lost among K total pieces on the ground. Each piece is represented as an N×N grid with '#' characters forming the shape and '.' characters as empty space.

The task is to identify which two pieces, when shifted horizontally and/or vertically and superimposed, exactly reconstruct the original figurine. The two pieces must not overlap (no shared '#' characters) and together must form the original shape precisely. Pieces cannot be rotated or flipped.

## Input Format

- First line: N (grid size) and K (number of pieces)
- Next N lines: the original figurine grid
- Next K×N lines: K grids describing the K pieces found

## Output Format

Two space-separated integers (in sorted order) indicating which two pieces reconstruct the original figurine.

## Sample Input

```
4 3
####
#..#
#.##
....
.#..
.#..
##..
....
####
##..
#..#
####
....
.###
.#..
.#..
```

## Sample Output

```
1 3
```
