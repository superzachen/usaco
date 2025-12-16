# USACO 2022 February Contest, Bronze: Problem 1 - Sleeping in Class

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=1203)

## Problem Description

Bessie frequently falls asleep during class lectures. Elsie is tracking the number of times Bessie falls asleep during N class periods. To make it appear that Bessie falls asleep consistently, Elsie wants to modify the log by combining adjacent class periods (merging their values) until all entries are equal.

For example, combining adjacent periods adds their sleep counts together into a single entry. The goal is to determine the minimum number of such merge operations needed to make all log entries identical.

## Input Format

- First line: T (number of test cases, where 1 ≤ T ≤ 10)
- For each test case:
  - First line: N (number of class periods, where 1 ≤ N ≤ 10⁵)
  - Second line: N space-separated integers representing sleep counts for each period

Constraints: Sum of all values ≤ 10⁶; sum of N across all test cases ≤ 10⁵

## Output Format

For each test case, output a single integer representing the minimum number of merge operations required.

## Sample Input

```
3
6
1 2 3 1 1 1
3
2 2 3
5
0 0 0 0 0
```

## Sample Output

```
3
2
0
```

## Sample Explanations

- **Test Case 1**: Merge operations transform [1,2,3,1,1,1] → [3,3,1,1,1] → [3,3,2,1] → [3,3,3] (3 operations)
- **Test Case 2**: Transform [2,2,3] → [2,5] → [7] (2 operations)
- **Test Case 3**: [0,0,0,0,0] already has equal entries (0 operations)
