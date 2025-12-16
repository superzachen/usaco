# USACO 2017 December Contest, Bronze: Problem 3 - Milk Measurement

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=761)

## Problem Description

Three cows (Bessie, Elsie, and Mildred) each initially produce 7 gallons of milk daily. Over 100 days, Farmer John records periodic measurements showing changes in each cow's milk output. These measurements are not necessarily recorded in chronological order.

Farmer John displays a picture of whichever cow(s) currently have the highest milk output. The task is to determine how many days require a display change.

## Input Format

- First line: N (number of measurements)
- Next N lines: Each contains a day (1-100), cow name, and change in milk output (nonzero integer)
- Milk output always remains in range 0-1000

File: `measurement.in`

## Output Format

Output a single integer representing the number of days requiring a display adjustment.

File: `measurement.out`

## Sample Input

```
4
7 Mildred +3
4 Elsie -1
9 Mildred -1
1 Bessie +2
```

## Sample Output

```
3
```

## Sample Explanation

Initially all cows produce 7 gallons. Day 1: Bessie reaches 9 (change). Day 4: Elsie drops to 6 (no change—Bessie still leads). Day 7: Mildred reaches 10 (change). Day 9: Mildred drops to 9, tying with Bessie (change).
