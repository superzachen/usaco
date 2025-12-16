# USACO 2015 December Contest, Bronze: Problem 3 - Contaminated Milk

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=569)

## Problem Description

At a milk-tasting party with N friends, exactly one of M milk types has spoiled. The organizer has records of who consumed which milk and when, plus information about who became ill and when. The task is to determine which milk types could potentially be contaminated, then calculate the minimum medicine doses needed to treat all possible victims across all viable scenarios.

A milk is a suspect if everyone who got sick drank it before becoming ill. For each suspect milk, count how many people drank it (including the already-sick). The answer is the maximum count across all suspect milks.

## Input Format

- Line 1: Four integers N, M, D, S
  - N: number of people (1 ≤ N ≤ 50)
  - M: milk types (1 ≤ M ≤ 50)
  - D: drinking records (1 ≤ D ≤ 1000)
  - S: illness reports (1 ≤ S ≤ N)
- Next D lines: Three integers p, m, t (person p drank milk m at time t)
- Next S lines: Two integers p, t (person p became sick at time t)

## Output Format

A single integer representing the minimum medicine doses needed.

## Sample Input

```
3 4 7 2
1 1 1
1 4 1
1 3 4
1 2 2
3 1 3
2 1 5
2 2 7
1 3
2 8
```

## Sample Output

```
3
```
