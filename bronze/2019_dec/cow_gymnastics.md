# USACO 2019 December Contest, Bronze: Problem 1 - Cow Gymnastics

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=963)

## Problem Description

Bessie coaches N cows through K practice sessions, ranking them in each. A pair of distinct cows is "consistent" if one cow consistently outperformed the other across all sessions. The task is to count all such consistent pairs.

## Input Format

The first line contains two integers K and N (1 ≤ K ≤ 10, 1 ≤ N ≤ 20). The next K lines each contain a permutation of integers 1 through N representing the rankings for that session. Earlier positions indicate better performance.

## Output Format

Output a single integer: the total number of consistent pairs.

## Sample Input

```
3 4
4 1 2 3
4 1 3 2
4 2 1 3
```

## Sample Output

```
4
```

## Sample Explanation

The consistent pairs are (1,4), (2,4), (3,4), and (1,3). These pairs maintain the same ranking order across all three sessions.
