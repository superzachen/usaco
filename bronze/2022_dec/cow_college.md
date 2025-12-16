# USACO 2022 December Contest, Bronze: Problem 1 - Cow College

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=1251)

## Problem Description

Farmer John is establishing a university for cows and needs to determine optimal tuition pricing. He has N cows, each willing to pay a maximum tuition of cᵢ. Farmer John sets a single tuition rate that all attending cows must pay. Any cow unwilling to pay that rate will not attend. The goal is to maximize revenue while identifying the optimal tuition charge.

**Note:** This problem may require 64-bit integer data types due to large values.

## Input Format

- First line: integer N (1 ≤ N ≤ 10⁵)
- Second line: N integers c₁, c₂, ..., cₙ representing each cow's maximum willingness to pay (1 ≤ cᵢ ≤ 10⁶)

## Output Format

Output two values: the maximum revenue Farmer John can generate and the corresponding optimal tuition. If multiple tuition amounts yield the same maximum revenue, output the smallest tuition value.

## Sample Input

```
4
1 6 4 6
```

## Sample Output

```
12 4
```

## Sample Explanation

At a tuition of $4, three cows will attend (those with maximum willingness of 6, 4, and 6), generating revenue of 3 × 4 = $12.
