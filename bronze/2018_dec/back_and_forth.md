# USACO 2018 December Contest, Bronze: Problem 3 - Back and Forth

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=857)

## Problem Description

Farmer John operates two barns, each with a 1000-gallon milk tank and 10 buckets. Starting with 1000 gallons in each tank:

- **Tuesday**: Takes a bucket from barn 1, fills it, carries milk to barn 2
- **Wednesday**: Takes a bucket from barn 2, fills it, carries milk to barn 1
- **Thursday**: Takes a bucket from barn 1, fills it, carries milk to barn 2
- **Friday**: Takes a bucket from barn 2, fills it, carries milk to barn 1

After Friday, he measures the milk in barn 1's tank. The task is to determine how many different possible readings are achievable.

## Input Format

Two lines of input:
- Line 1: 10 integers representing bucket sizes initially at barn 1
- Line 2: 10 integers representing bucket sizes initially at barn 2

All bucket sizes range from 1 to 100 gallons.

## Output Format

A single integer representing the count of distinct possible final measurements in barn 1's tank.

## Sample Input

```
1 1 1 1 1 1 1 1 2
5 5 5 5 5 5 5 5 5 5
```

## Sample Output

```
5
```

## Sample Explanation

Five possible outcomes for barn 1's final measurement:
- 1000 gallons (same bucket carried back and forth)
- 1003 gallons (carry 2, then 5 out, then 1, then 1)
- 1004 gallons (carry 1, then 5 out, then 1, then 1)
- 1007 gallons (carry 1, then 5 out, then 2, then 5)
- 1008 gallons (carry 1, then 5 out, then 1, then 5)
