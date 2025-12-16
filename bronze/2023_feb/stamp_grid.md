# USACO 2023 February Contest, Bronze: Problem 2 - Stamp Grid

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=1300)

## Problem Description

Bessie wants to create a desired stamp painting on an N×N canvas using a single K×K stamp. She can rotate the stamp clockwise by 90° and stamp it anywhere on the grid as long as the stamp remains entirely within bounds. When stamping at position (i,j), each inked cell on the stamp paints the corresponding cell on the canvas black. Once a cell is painted black, it remains black. The task is to determine if Bessie can recreate the desired painting with the given stamp.

## Input Format

- First line: T (number of test cases, 1 ≤ T ≤ 100)
- For each test case:
  - Integer N followed by N lines of N characters each (* for inked, . for blank) representing the desired painting
  - Integer K followed by K lines of K characters each representing the stamp

## Output Format

For each test case, output "YES" or "NO" on separate lines.

## Sample Input

```
4
2
**
*.
1
*
3
.**
.**
***
2
.*
*.
3
...
.*.
...
2
.*
*.
3
**.
.**
..*
2
.*
*.
```

## Sample Output

```
YES
YES
NO
YES
```
