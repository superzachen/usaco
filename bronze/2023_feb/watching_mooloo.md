# USACO 2023 February Contest, Bronze: Problem 3 - Watching Mooloo

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=1301)

## Problem Description

Bessie needs to plan her Mooloo subscription across N days. The service charges `d + K` moonies for a subscription covering `d` consecutive days. Subscriptions can start anytime and be renewed multiple times. The goal is to minimize total cost while covering all N planned viewing days.

**Note:** This problem requires 64-bit integer data types due to large values involved.

## Input Format

- Line 1: Two integers N and K
- Line 2: N integers representing viewing days (in ascending order, with constraints: 1 ≤ d₁ < d₂ < ... < dₙ ≤ 10¹⁴)

## Output Format

A single integer representing the minimum moonies Bessie needs to spend.

## Sample Input 1

```
2 4
7 9
```

## Sample Output 1

```
7
```

**Explanation:** A three-day subscription starting day 7 costs 3 + 4 = 7 moonies, covering both days.

## Sample Input 2

```
2 3
1 10
```

## Sample Output 2

```
8
```

**Explanation:** Two separate one-day subscriptions: day 1 (1+3=4 moonies) and day 10 (1+3=4 moonies), totaling 8 moonies.
