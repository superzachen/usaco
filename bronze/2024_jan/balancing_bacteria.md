# USACO 2024 January Contest, Bronze: Problem 3 - Balancing Bacteria

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=1373)

## Problem Description

Farmer John manages N patches of grass, each with bacteria level deviation `a_i` from healthy grass. He has two pesticides: one adds bacteria, one removes it. When sprayed from patch N with power level L:
- Patch N receives L units
- Patch N-1 receives L-1 units
- Patch N-2 receives L-2 units
- Patches 1 through N-L receive no effect

The goal is to make every patch have healthy bacteria levels using the minimum number of spray applications.

## Input Format

- Line 1: Integer N (1 ≤ N ≤ 2×10⁵)
- Line 2: N integers representing initial bacteria deviations (-10¹⁵ ≤ a_i ≤ 10¹⁵)

## Output Format

A single integer: the minimum number of spray applications needed.

## Sample Input 1

```
2
-1 3
```

## Sample Output 1

```
6
```

**Explanation:** Apply remove-bacteria spray (L=1) five times, then add-bacteria spray (L=2) once.

## Sample Input 2

```
5
1 3 -2 -7 5
```

## Sample Output 2

```
26
```
