# USACO 2017 February Contest, Bronze: Problem 1 - Why Did the Cow Cross the Road

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=711)

## Problem Description

Farmer John is documenting cow road crossings for a university study. He records N observations during one day, each noting a cow's ID (1-10) and which side of the road it's on (0 or 1). The task is to count confirmed crossings, defined as consecutive sightings of the same cow on different sides of the road.

## Input Format

- First line: N (positive integer, at most 100) - number of observations
- Next N lines: Each contains a cow ID and position (0 or 1)
- File: `crossroad.in`

## Output Format

- Single integer representing total confirmed crossings
- File: `crossroad.out`

## Sample Input

```
8
3 1
3 0
6 0
2 1
4 1
3 0
4 0
3 1
```

## Sample Output

```
3
```

## Sample Explanation

Cow 3 crosses twice: appears on side 1, then side 0, then back to side 1. Cow 4 crosses once. Cows 2 and 6 don't cross (only appear on one side each).
