# USACO 2014 December Contest, Bronze: Problem 3 - Cow Jog

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=489)

## Problem Description

N cows are jogging on a single-lane track at different speeds and starting positions. Since cows cannot pass each other, when a faster cow catches up to a slower one, it must slow down to match that cow's speed, forming a group. The task is to determine how many distinct groups will remain once all cows have settled into their final groupings.

## Input Format

- First line: integer N (1 ≤ N ≤ 100,000)
- Following N lines: position and speed for each cow
- Position: non-negative integer (≤ 1 billion)
- Speed: positive integer (≤ 1 billion)
- Cows are given in increasing order of starting position, all positions distinct

## Output Format

A single integer representing the number of final groups.

## Sample Input

```
5
0 1
1 2
2 3
3 2
6 1
```

## Sample Output

```
2
```

## Explanation

The solution involves determining which cows will eventually merge into the same group. A cow with higher speed starting behind another will catch up and join its group unless blocked by a faster cow ahead.
