# USACO 2021 US Open Contest, Bronze: Problem 2 - Acowdemia II

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=1132)

## Problem Description

Bessie needs to determine the relative seniority of N lab members by analyzing K publications. Each publication lists all N members in order of decreasing effort contributed, with ties broken alphabetically. The key constraint is that more senior researchers never contribute more effort than junior ones.

Given the publication author lists, determine which seniority relationships can be definitively established.

## Input Format

- Line 1: Two integers K and N (number of publications and lab members)
- Line 2: N space-separated strings (member names, lowercase letters, ≤10 characters)
- Next K lines: N space-separated strings (author lists for each publication)

## Output Format

N lines with N characters each:
- For line i, character j: `1` if member i is definitely more senior than member j
- `0` if member i is definitely more junior than member j
- `?` if the relationship cannot be determined
- `B` for position i,i (Bessie's favorite letter)

## Sample Input 1

```
1 3
dean elsie mildred
elsie mildred dean
```

## Sample Output 1

```
B11
0B?
0?B
```

## Sample Input 2

```
2 3
elsie mildred dean
elsie mildred dean
elsie dean mildred
```

## Sample Output 2

```
B00
1B0
11B
```
