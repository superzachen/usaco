# USACO 2016 December Contest, Bronze: Problem 2 - Block Game

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=664)

## Problem Description

Farmer John has N spelling boards, each with a different word on each side. When boards are placed on the ground, N words are visible. By flipping boards, different word combinations can be exposed.

FJ wants to create wooden blocks with alphabet letters. He needs enough blocks of each letter so that the cows can spell any possible set of N visible words, regardless of which side of each board faces up.

For example, with boards showing "box," "cat," and "car," the cows would need: 1 'b', 1 'o', 1 'x', 2 'c's, 2 'a's, 1 't', and 1 'r'.

The goal is to find the minimum number of blocks needed for each letter across all 2^N possible board configurations.

## Input Format

- Line 1: Integer N (1 ≤ N ≤ 100)
- Next N lines: Two space-separated words (each up to 10 lowercase letters), representing opposite sides of a board

## Output Format

26 lines, each containing a number representing the required quantity of blocks for letters 'a' through 'z' in order.

## Sample Input

```
3
fox box
dog cat
car bus
```

## Sample Output

```
2
2
2
1
0
1
1
0
0
0
0
0
0
0
2
0
0
1
1
1
1
0
0
1
0
0
```
