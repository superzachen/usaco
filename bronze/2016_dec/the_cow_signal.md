# USACO 2016 December Contest, Bronze: Problem 3 - The Cow-Signal

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=665)

## Problem Description

Bessie and her cow friends are playing as superhero characters and need to enlarge a signal. A special signal is drawn on an M × N sheet of paper using only '.' and 'X' characters. The task is to amplify the signal to be exactly K times bigger in each direction.

## Input Format

- First line contains M, N, and K (separated by spaces)
  - M: number of rows (1 ≤ M ≤ 10)
  - N: number of columns (1 ≤ N ≤ 10)
  - K: amplification factor (1 ≤ K ≤ 10)
- Next M lines contain length-N strings describing the signal

## Output Format

Output KM lines, each with KN characters, showing the enlarged signal.

## Sample Input

```
5 4 2
XXX.
X..X
XXX.
X..X
XXX.
```

## Sample Output

```
XXXXXX..
XXXXXX..
XX....XX
XX....XX
XXXXXX..
XXXXXX..
XX....XX
XX....XX
XXXXXX..
XXXXXX..
```
