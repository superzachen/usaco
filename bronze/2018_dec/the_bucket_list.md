# USACO 2018 December Contest, Bronze: Problem 2 - The Bucket List

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=856)

## Problem Description

Farmer John needs to determine the minimum number of buckets required to milk all his cows. Each cow requires milking during a specific time interval and needs a certain number of buckets. When multiple cows are milked simultaneously, they cannot share buckets. FJ's strategy is to assign the lowest-numbered available buckets when each cow's milking begins.

## Input Format

- First line: integer N (1 ≤ N ≤ 100) representing the number of cows
- Next N lines: three integers per line: sᵢ (start time), tᵢ (end time), and bᵢ (buckets needed)
- Both sᵢ and tᵢ are in range 1 to 1000; bᵢ is in range 1 to 10
- All sᵢ and tᵢ values are distinct

## Output Format

A single integer representing the total number of buckets needed in storage.

## Sample Input

```
3
4 10 1
8 13 3
2 6 2
```

## Sample Output

```
4
```

## Explanation

Cow 3 uses buckets 1-2 (times 2-6). Cow 1 uses bucket 3 (times 4-10). Cow 2, starting at time 8, cannot use bucket 3 (still in use), so it uses buckets 1, 2, and 4. The maximum needed is 4 total buckets.
