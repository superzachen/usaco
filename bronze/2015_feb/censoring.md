# USACO 2015 February Contest, Bronze: Problem 1 - Censoring

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=526)

## Problem Description

Farmer John wants to remove inappropriate content from a magazine subscription. He has a string S and needs to repeatedly find and delete the first occurrence of substring T until no occurrences remain. The challenge is that deleting one occurrence might create new occurrences of T.

## Input Format

- Line 1: String S (length ≤ 10^6 characters)
- Line 2: String T (length ≤ 100 characters, ≤ length of S)
- All characters are lowercase letters (a-z)

## Output Format

The final string S after all occurrences of T have been deleted. The result is guaranteed to be non-empty.

## Sample Input

```
whatthemomooofun
moo
```

## Sample Output

```
whatthefun
```

## Explanation

The string contains "moo" three times. Removing the first occurrence ("whatthe**moo**oofun" → "whattheoofun"), then the next ("whatthe**oo**fun" → "whatthefun"), and finally checking confirms no more occurrences exist.
