# USACO 2023 February Contest, Bronze: Problem 1 - Hungry Cow

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=1299)

## Problem Description

Bessie the cow eats one haybale daily if available. Farmer John sends haybale deliveries on specific days. On day dᵢ, a delivery of bᵢ haybales arrives in the morning (before dinner). Given N deliveries and T total days, calculate how many haybales Bessie eats.

**Constraints:**
- 1 ≤ N ≤ 10⁵, 1 ≤ T ≤ 10¹⁴
- 1 ≤ dᵢ ≤ 10¹⁴, 1 ≤ bᵢ ≤ 10⁹
- Days are ordered: 1 ≤ d₁ < d₂ < ... < dₙ ≤ T

## Input Format

First line: N and T
Next N lines: dᵢ and bᵢ (day and quantity of delivery)

## Output Format

A single integer representing total haybales eaten during the first T days.

## Sample Input 1

```
1 5
1 2
```

## Sample Output 1

```
2
```

Two haybales arrive day 1; Bessie eats on days 1–2, then none available.

## Sample Input 2

```
2 5
1 2
5 10
```

## Sample Output 2

```
3
```

Two haybales day 1 (eaten days 1–2); ten arrive day 5 (one eaten).

## Sample Input 3

```
2 5
1 10
5 10
```

## Sample Output 3

```
5
```

Ten haybales day 1 (eaten days 1–4); ten more day 5 (sixteen total, one eaten day 5).
