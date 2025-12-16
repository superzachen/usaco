# USACO 2021 December Contest, Bronze: Problem 1 - Lonely Photo

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=1155)

## Problem Description

Farmer John has N new cows (where 3 ≤ N ≤ 5×10⁵), each either a Guernsey or Holstein breed. The cows stand in a line, and FJ wants to photograph every sequence of three or more consecutive cows.

However, FJ discards "lonely" photos—those containing exactly one cow of a particular breed. The task is to count how many such lonely photos are discarded.

Two photos differ if they begin or end at different positions in the lineup.

## Input Format

- First line: integer N (number of cows)
- Second line: string of N characters, where 'G' represents Guernsey and 'H' represents Holstein

## Output Format

Print the count of lonely photos that will be discarded.

## Sample Input

```
5
GHGHG
```

## Sample Output

```
3
```

## Explanation

All three-character substrings (GHG, HGH, GHG) each contain exactly one cow of one breed, making them lonely photos. Longer substrings are acceptable.
