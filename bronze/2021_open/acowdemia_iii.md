# USACO 2021 US Open Contest, Bronze: Problem 3 - Acowdemia III

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=1133)

## Problem Description

Bessie needs to form friendships in a 2D pasture grid where cells contain cows (C), grass (G), or empty space (.). Two distinct cows can become friends by meeting at an adjacent grass cell (horizontally or vertically adjacent to both). When cows meet, they consume the grass, preventing future use of that meeting point. Each pair can meet at most once, though individual cows can befriend multiple others.

The goal is to determine the maximum number of friendships (cow pairs) that can form.

## Input Format

- First line: N and M (where N, M ≤ 1000)
- Next N lines: strings of M characters representing the pasture grid

## Output Format

A single integer representing the maximum number of cow pairs that can become friends.

## Sample Input

```
4 5
.CGGC
.CGCG
CGCG.
.CC.C
```

## Sample Output

```
4
```

## Sample Explanation

Four friendships form through these meetings:
- Cows at (2,2) and (3,3) meet at grass (3,2)
- Cows at (2,2) and (2,4) meet at grass (2,3)
- Cows at (2,4) and (3,3) meet at grass (3,4)
- Cows at (2,4) and (1,5) meet at grass (2,5)
