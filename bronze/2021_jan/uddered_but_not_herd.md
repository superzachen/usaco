# USACO 2021 January Contest, Bronze: Problem 1 - Uddered but not Herd

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=1083)

## Problem Description

Cows have their own alphabet ordering (the "cowphabet") consisting of letters 'a' through 'z' in a specific sequence that may differ from the standard alphabet. Bessie repeatedly hums this cowphabet, and Farmer John hears only some of the letters she hums.

Given the cowphabet ordering and a string of letters Farmer John heard, determine the minimum number of complete cowphabet cycles Bessie must have hummed to produce that string.

## Input Format

- Line 1: The 26 lowercase letters 'a' through 'z' arranged in cowphabet order
- Line 2: A string of lowercase letters (length 1–1000) that Farmer John heard

## Output Format

Print the minimum number of times Bessie must have hummed the entire cowphabet.

## Sample Input

```
abcdefghijklmnopqrstuvwxyz
mood
```

## Sample Output

```
3
```

## Explanation

With the standard alphabet ordering, the string "mood" requires at least 3 complete cycles of the cowphabet to be hummed, as shown by tracking the positions of 'm', 'o', 'o', and 'd' across repetitions.
