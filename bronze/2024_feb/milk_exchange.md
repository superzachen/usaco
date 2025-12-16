# USACO 2024 February Contest, Bronze: Problem 2 - Milk Exchange

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=1396)

## Problem Description

Farmer John has N cows arranged in a circle, each with a bucket of capacity aᵢ liters, all initially full. Every minute, cows exchange milk based on a string of 'L' and 'R' characters. If sᵢ is 'L', cow i passes 1 liter left; if 'R', cow i passes 1 liter right (provided the cow has at least 1 liter). All exchanges happen simultaneously. Any milk exceeding a bucket's capacity is lost. Determine the total milk remaining after M minutes.

## Input Format

- Line 1: Two integers N and M
- Line 2: String s₁s₂...sₙ of 'L' and 'R' characters
- Line 3: N integers representing bucket capacities a₁, a₂, ..., aₙ

## Output Format

A single integer representing the total milk remaining after M minutes.

## Sample Input 1

```
3 1
RRL
1 1 1
```

## Sample Output 1

```
2
```

**Explanation:** Cows 2 and 3 exchange milk without loss. Cow 1's milk causes overflow at cow 2's bucket, losing 1 liter.

## Sample Input 2

```
5 20
LLLLL
3 3 2 3 3
```

## Sample Output 2

```
14
```

**Explanation:** Each cow passes left and receives from the right, preserving all milk regardless of time elapsed.

## Sample Input 3

```
9 5
RRRLRRLLR
5 8 4 9 3 4 9 5 4
```

## Sample Output 3

```
38
```

**Explanation:** Starting with 51 liters total, cows 3, 6, and 7 lose 5, 3, and 5 liters respectively after 5 minutes, leaving 38 liters.
