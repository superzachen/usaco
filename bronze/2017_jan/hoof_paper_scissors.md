# USACO 2017 January Contest, Bronze: Problem 2 - Hoof, Paper, Scissors

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=688)

## Problem Description

Two cows play a series of N games using gestures representing hoof, paper, or scissors. The rules follow standard rock-paper-scissors logic: hoof beats scissors, scissors beats paper, and paper beats hoof. Farmer John observes the games but cannot identify which gesture corresponds to which move—he labels them 1, 2, and 3 instead.

Given the sequence of gestures made by both cows, determine the maximum number of games the first cow could have won by finding the optimal mapping of numbers to moves.

## Input Format

- First line: integer N (1 ≤ N ≤ 100)
- Next N lines: two integers each (values 1, 2, or 3) representing the gestures of cow 1 and cow 2 in each game

**Input file:** `hps.in`

## Output Format

Print the maximum possible number of games won by the first cow.

**Output file:** `hps.out`

## Sample Input

```
5
1 2
2 2
1 3
1 1
3 2
```

## Sample Output

```
2
```

## Sample Explanation

One solution assigns gesture 1 as scissors, 2 as hoof, and 3 as paper. This yields 2 wins for cow 1 (from rounds "1 3" and "3 2"). No other assignment produces more victories.
