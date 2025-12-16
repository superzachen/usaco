# USACO 2015 US Open Contest, Bronze: Problem 1 - Moocryption

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=545)

## Problem Description

Cows have created a word finder puzzle where the word "MOO" appears horizontally, vertically, or diagonally in various locations. The puzzle contents have been encrypted using a substitution cipher where each letter maps to a different letter, and no letter maps to itself.

Given an encrypted puzzle, determine the maximum possible number of times "MOO" could appear if decrypted with an appropriate substitution cipher.

## Input Format

The first line contains N and M, the number of rows and columns (both at most 50). The next N lines each contain M uppercase letters representing one row of the encrypted puzzle.

## Output Format

Output the maximum possible number of "MOO" instances that could exist in the decrypted puzzle with an appropriate substitution cipher.

## Sample Input

```
4 6
TAMHGI
MMQVWM
QMMQSM
HBQUMQ
```

## Sample Output

```
6
```

## Sample Explanation

The sample input represents an encrypted version of the puzzle shown at the problem's beginning. After applying the cipher where "M" maps to "O" and "Q" maps to "M", the decrypted puzzle contains 6 instances of "MOO".
