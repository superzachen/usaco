# USACO 2018 January Contest, Bronze: Problem 3 - Out of Place

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=785)

## Problem Description

Farmer John wants to photograph his herd with cows lined up from shortest to tallest. After arranging them properly, Bessie steps out and reinserts herself elsewhere in the lineup. FJ needs to determine the minimum number of swaps required to restore the correct sorted order.

## Input Format

- First line: N (the number of cows, where 2 ≤ N ≤ 100)
- Next N lines: Individual integers representing each cow's height (range: 1 to 1,000,000)
- Note: Multiple cows may share the same height

## Output Format

A single integer representing the minimum number of pair swaps needed to sort the lineup.

## Sample Input

```
6
2
4
7
7
9
3
```

## Sample Output

```
3
```

## Sample Explanation

The original lineup is: `2 4 7 7 9 3`

The solution demonstrates three swaps to achieve sorted order `2 3 4 7 7 9`:
1. Swap positions 5 and 6: `2 4 7 7 3 9`
2. Swap the `7` and `3`: `2 4 3 7 7 9`
3. Swap `4` and `3`: `2 3 4 7 7 9`
