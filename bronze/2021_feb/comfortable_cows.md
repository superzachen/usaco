# USACO 2021 February Contest, Bronze: Problem 2 - Comfortable Cows

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=1108)

## Problem Description

Farmer John manages a large 2D grid pasture where he adds N cows one by one. Each cow occupies a distinct cell at coordinates (xᵢ, yᵢ). A cow is considered "comfortable" when it has exactly three adjacent cows (horizontally or vertically neighboring). The task is to count comfortable cows after each new cow is added.

## Input Format

- First line: integer N (1 ≤ N ≤ 10^5)
- Next N lines: two space-separated integers representing (x, y) coordinates of each cow (0 ≤ x, y ≤ 1000)
- All coordinates are distinct

## Output Format

N lines, where line i contains the total count of comfortable cows after adding the i-th cow.

## Sample Input

```
8
0 1
1 0
1 1
1 2
2 1
2 2
3 1
3 2
```

## Sample Output

```
0
0
0
1
0
0
1
2
```

## Sample Explanation

- After cow 4 is added: the cow at (1,1) becomes comfortable
- After cow 7 is added: the cow at (2,1) becomes comfortable
- After cow 8 is added: both cows at (2,1) and (2,2) are comfortable
