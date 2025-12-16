# USACO 2020 January Contest, Bronze: Problem 1 - Word Processor

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=987)

## Problem Description

Bessie needs to format an essay using specific word-wrapping rules. The essay contains N words, and each line must contain no more than K characters (excluding spaces). The word processor follows this strategy: if a word fits on the current line, place it there; otherwise, start a new line. Words on the same line are separated by single spaces, with no trailing spaces.

## Input Format

- Line 1: Two space-separated integers N and K
  - N: number of words (1 ≤ N ≤ 100)
  - K: maximum characters per line (1 ≤ K ≤ 80)
- Line 2: N words separated by spaces (each word: 1-15 characters, uppercase/lowercase letters only)
- Constraint: No word exceeds K characters

## Output Format

The formatted essay with proper line breaks according to the specified rules.

## Sample Input

```
10 7
hello my name is Bessie and this is my essay
```

## Sample Output

```
hello my
name is
Bessie
and this
is my
essay
```

## Explanation

The first line "hello my" contains 7 non-space characters. Adding "name" would exceed the 7-character limit, so it moves to the next line.
