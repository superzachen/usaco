# USACO 2019 February Contest, Bronze: Problem 1 - Sleepy Cow Herding

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=915)

## Problem Description

Farmer John needs to herd three cows together into consecutive positions on a number line. The cows can only be moved if they are at the minimum or maximum position among all three cows. When moved, a cow must go to an unoccupied integer location where it is no longer an endpoint. The challenge is to determine both the minimum and maximum number of moves needed to group the three cows into three consecutive locations.

## Input Format

One line containing three space-separated integers representing the locations of Bessie, Elsie, and Mildred. Each location is an integer in the range 1 to 10⁹.

## Output Format

- First line: minimum number of moves needed
- Second line: maximum number of moves possible

## Sample Input

```
4 7 9
```

## Sample Output

```
1
2
```

## Explanation

The minimum is 1 move—moving the cow at position 4 to position 8 creates consecutive positions 7, 8, 9. The maximum is 2 moves—for example, moving the cow at position 9 to position 6, then moving the cow at position 7 to position 5.
