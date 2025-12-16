# USACO 2014 December Contest, Bronze: Problem 2 - Crosswords

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=488)

## Problem Description

Bessie needs help recovering clue numbering in a crossword puzzle where the original numbering has been obscured. Given an N by M grid with clear cells (.) and blocked cells (#), the task is to identify which cells begin clues and assign them sequential numbers.

A cell begins a horizontal clue if it's clear, has a blocked/outside cell to its left, and has two clear cells to its right. A cell begins a vertical clue using analogous rules: blocked/outside cell above, two clear cells below. This ensures clues represent words of 3+ characters.

Cells are numbered sequentially (1, 2, 3...) in reading order: left to right across rows, top to bottom.

## Input Format

- First line: N and M (grid dimensions, 3 ≤ N, M ≤ 50)
- Next N lines: M characters each ('.' for clear, '#' for blocked)

## Output Format

- First line: Total number of clues
- Following lines: Row and column position of each clue (1-indexed), in reading order

## Sample Input

```
5 3
...
#..
...
..#
.##
```

## Sample Output

```
4
1 1
1 2
1 3
3 1
```
