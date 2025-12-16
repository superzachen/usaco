# USACO 2022 February Contest, Bronze: Problem 3 - Blocks

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=1205)

## Problem Description

Bessie has four wooden blocks, each a cube with six letters on its sides. She arranges blocks in a row to spell words by displaying letters on top. Given the letters available on each block and a list of target words, determine which words she can spell. Each block can only be used once per word.

## Input Format

- Line 1: N (number of words to check, 1 ≤ N ≤ 10)
- Lines 2-5: Six uppercase letters each, representing the sides of the four blocks
- Lines 6 to N+5: Words to spell (1-4 uppercase letters each)

## Output Format

For each word, output "YES" if it can be spelled using the blocks, "NO" otherwise.

## Sample Input

```
6
MOOOOO
OOOOOO
ABCDEF
UVWXYZ
COW
MOO
ZOO
MOVE
CODE
FARM
```

## Sample Output

```
YES
NO
YES
YES
NO
NO
```

## Explanation

Bessie can spell COW, ZOO, and MOVE. She cannot spell MOO (the M block cannot simultaneously provide an O), FARM (no R available), or CODE (C, D, and E are all on the same block).
