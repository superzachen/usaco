# USACO 2016 January Contest, Bronze: Problem 1 - Promotion Counting

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=591)

## Problem Description

Participants in the USA Cow Olympiad start in the bronze division and advance through silver, gold, and platinum divisions by scoring perfectly on contests. Farmer John needs to determine how many promotions occurred between divisions based on participant counts before and after a contest.

The task is to deduce promotion numbers using only the participant counts at each division level before and after the contest.

## Input Format

Four lines, each containing two integers (range 0 to 1,000,000):
- Line 1: Bronze participants before and after
- Line 2: Silver participants before and after
- Line 3: Gold participants before and after
- Line 4: Platinum participants before and after

## Output Format

Three lines, each with a single integer:
- Line 1: Promotions from bronze to silver
- Line 2: Promotions from silver to gold
- Line 3: Promotions from gold to platinum

## Sample Input

```
1 2
1 1
1 1
1 2
```

## Sample Output

```
1
1
1
```

## Sample Explanation

One participant was in each division initially. The final state shows 2 bronze and 2 platinum participants. This could occur if 2 new participants joined—one advanced through all divisions to platinum, while another remained in bronze.
