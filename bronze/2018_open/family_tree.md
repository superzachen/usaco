# USACO 2018 US Open Contest, Bronze: Problem 3 - Family Tree

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=833)

## Problem Description

Farmer John maintains records of cow genealogy spanning multiple generations. Given two cows and their family relationships, determine how these cows relate to each other.

## Input Format

- **Line 1:** Integer N (1 ≤ N ≤ 100) followed by two cow names to analyze
- **Lines 2 to N+1:** Each line contains two names X and Y, indicating "X is the mother of Y"
- Cow names are strings of at most 10 uppercase letters

## Output Format

Determine the relationship between the two query cows:

- **SIBLINGS:** if they share the same mother
- **Direct descendant:** output format is "ELSIE is the (relation) of BESSIE" where relation includes "mother," "grand-mother," "great-grand-mother," etc.
- **Aunt relationship:** "ELSIE is the [great-]aunt of BESSIE" (with appropriate number of "great-" prefixes)
- **Cousins:** if they share a common ancestor but don't fit other categories
- **NOT RELATED:** if no common ancestry exists

## Sample Input

```
7 AA BB
MOTHER AA
GGMOTHER BB
MOTHER SISTER
GMOTHER MOTHER
GMOTHER AUNT
AUNT COUSIN
GGMOTHER GMOTHER
```

## Sample Output

```
BB is the great-aunt of AA
```
