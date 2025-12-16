# USACO 2022 January Contest, Bronze: Problem 2 - Non-Transitive Dice

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=1180)

## Problem Description

The cows play a dice game where two dice are rolled and the higher number wins. If tied, they reroll until there's a winner. Die X "beats" die Y if X is more likely to win.

The problem presents three example 4-sided dice:
- Die A: 4, 5, 6, 7
- Die B: 2, 4, 5, 10
- Die C: 1, 4, 8, 9

These form a non-transitive set: A beats B, B beats C, and C beats A. This means each die beats exactly one other die and loses to another—no die dominates the others.

Given dice A and B, determine if a third die C can be created to form a non-transitive set. All face values must be integers from 1-10 inclusive.

## Input Format

First line contains T (1 ≤ T ≤ 10), the number of test cases. Each subsequent line contains 8 numbers: the four faces of die A followed by the four faces of die B. All values range from 1-10.

## Output Format

Output T lines, each containing "yes" or "no" indicating whether a valid die C exists for that test case.

## Sample Input

```
3
4 5 6 7 2 4 5 10
2 2 2 2 1 1 1 1
1 1 1 1 2 2 2 2
```

## Sample Output

```
yes
no
no
```
