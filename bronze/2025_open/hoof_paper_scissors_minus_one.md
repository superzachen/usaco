# USACO 2025 US Open Contest, Bronze: Problem 1 - Hoof Paper Scissors Minus One

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=1515)

## Problem Description

In this game variant, Bessie and Elsie each play two symbols (one per hoof). After all four symbols are revealed, each player chooses one of their two symbols to play. The outcome follows standard Hoof Paper Scissors rules based on a provided interaction chart.

Given Elsie's symbol combinations across M games, determine how many different symbol combinations guarantee Bessie wins each game. A combination is an ordered pair (L,R) where L and R are the left and right hoof symbols.

**Constraints:** 1 ≤ N ≤ 3000, 1 ≤ M ≤ 3000, time limit is 3 seconds.

## Input Format

- Line 1: Two integers N (number of symbols) and M (number of games)
- Next N lines: The i-th line contains i characters from {D, W, L}:
  - D: symbol i draws against symbol j
  - W: symbol i wins against symbol j
  - L: symbol i loses against symbol j
- Next M lines: Two integers s₁ and s₂ representing Elsie's symbol combination

## Output Format

M lines, where line i contains the count of symbol combinations guaranteeing Bessie wins game i.

## Sample Input

```
3 3
D
WD
LWD
1 2
2 3
1 1
```

## Sample Output

```
0
0
5
```

**Explanation:** With Rock-Paper-Scissors mapping (Hoof=1, Paper=2, Scissors=3), Bessie cannot guarantee wins against (1,2) or (2,3), but against (1,1) she can play any of five combinations: (2,2), (2,3), (2,1), (1,2), or (3,2) to guarantee victory.
