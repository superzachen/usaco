# USACO 2023 January Contest, Bronze: Problem 3 - Moo Operations

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=1277)

## Problem Description

Bessie receives Q strings containing only 'M' and 'O' characters. She wants to transform each string into "MOO" using the minimum number of operations. The allowed operations are:

1. Replace either the first or last character with its opposite ('M' ↔ 'O')
2. Delete either the first or last character

Determine the minimum operations needed for each string, or output -1 if transformation is impossible.

## Input Format

- First line: integer Q (1 ≤ Q ≤ 100)
- Next Q lines: strings containing only 'M' and 'O' characters, each 1-100 characters long

## Output Format

For each string, output the minimum number of operations required to form "MOO", or -1 if impossible.

## Sample Input

```
3
MOMMOM
MMO
MOO
```

## Sample Output

```
4
-1
0
```

## Sample Explanation

- For "MOMMOM": Replace last character with O, then delete first three characters (4 operations total).
- For "MMO": Cannot be transformed into "MOO".
- For "MOO": Already in target form (0 operations).
