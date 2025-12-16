# USACO 2015 US Open Contest, Bronze: Problem 4 - Palindromic Paths

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=548)

## Problem Description

Farmer John's farm consists of an N×N grid (2 ≤ N ≤ 18) where each field contains a letter. Bessie walks from the upper-left to lower-right field, moving only right or down, collecting letters to form a string. The challenge asks how many distinct palindromic strings Bessie can create along different paths.

## Input Format

- First line: integer N (grid size)
- Following N lines: N characters each representing the grid rows (letters A-Z)

## Output Format

A single integer representing the count of distinct palindromes Bessie can form.

## Sample Input

```
4
ABCD
BXZX
CDXB
WCBA
```

## Sample Output

```
4
```

## Explanation

For the given 4×4 grid, there are four distinct palindromic strings that can be formed through various paths from top-left to bottom-right: ABCDCBA, ABCWCBA, ABXZXBA, and ABXDXBA. Multiple routes may produce the same palindrome, but each unique palindrome counts only once.
