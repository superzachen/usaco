# USACO 2023 January Contest, Bronze: Problem 2 - Air Cownditioning II

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=1276)

## Problem Description

Farmer John needs to cool his cows during an exceptionally hot summer. He has N cows (1 ≤ N ≤ 20) in a barn with stalls numbered 1-100. Each cow i occupies stalls from sᵢ to tᵢ and requires temperature reduction of at least cᵢ units.

The barn has M air conditioners (1 ≤ M ≤ 10). Each air conditioner i:
- Costs mᵢ units to operate
- Cools stalls from aᵢ to bᵢ
- Reduces temperature by pᵢ units

The goal is to find the minimum cost to operate enough air conditioners so all cows meet their cooling requirements. It's guaranteed that using all conditioners will satisfy all cows.

## Input Format

- Line 1: N and M
- Next N lines: sᵢ, tᵢ, cᵢ (stall range and cooling requirement for each cow)
- Next M lines: aᵢ, bᵢ, pᵢ, mᵢ (range, power, and cost for each air conditioner)

## Output Format

A single integer representing the minimum cost needed to keep all cows comfortable.

## Sample Input

```
2 4
1 5 2
7 9 3
2 9 2 3
1 6 2 8
1 2 4 2
6 9 1 5
```

## Sample Output

```
10
```

**Explanation:** One optimal solution selects air conditioners cooling intervals [2,9], [1,2], and [6,9] for a combined cost of 3 + 2 + 5 = 10.
