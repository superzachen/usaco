# USACO 2018 US Open Contest, Bronze: Problem 1 - Team Tic Tac Toe

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=831)

## Problem Description

Farmer John has 26 cows named with letters A-Z. They play a multi-player tic-tac-toe variant on a 3×3 board where each square is marked with a cow's initial letter.

Victory conditions:
- **Individual victory**: A single cow claims an entire row, column, or diagonal
- **Team victory**: Two cows can win if any row, column, or diagonal contains only their letters AND both cows' letters appear in that line

The same board square may contribute to multiple victory claims.

## Input Format

Three lines, each containing three characters from the range A–Z.

## Output Format

Two lines:
- Line 1: Number of individual cows claiming victory
- Line 2: Number of two-cow teams claiming victory

## Sample Input

```
COW
XXO
ABC
```

## Sample Output

```
0
2
```

## Sample Explanation

No single cow occupies a complete row, column, or diagonal. However, two teams can win: (C,X) via the diagonal and (X,O) via the middle row.
