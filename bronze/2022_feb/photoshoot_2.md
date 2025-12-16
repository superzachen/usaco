# USACO 2022 February Contest, Bronze: Problem 2 - Photoshoot 2

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=1204)

## Problem Description

Farmer John needs to rearrange N cows from their current order to a desired target order. The cows are numbered 1 through N, and can only be moved left in the sequence (not right). The task is to determine the minimum number of individual cow moves needed to achieve the target arrangement.

## Input Format

- Line 1: Integer N (the number of cows, where 1 ≤ N ≤ 10⁵)
- Line 2: N space-separated integers representing the current arrangement (a₁, a₂, ..., aₙ)
- Line 3: N space-separated integers representing the desired arrangement (b₁, b₂, ..., bₙ)

## Output Format

Print a single integer representing the minimum number of modifications required.

## Sample Input 1

```
5
1 2 3 4 5
1 2 3 4 5
```

## Sample Output 1

```
0
```

## Sample Input 2

```
5
5 1 3 2 4
4 5 2 1 3
```

## Sample Output 2

```
2
```

Example transformation shown: Moving cow 4 left four positions, then cow 2 left two positions transforms the sequence from `5 1 3 2 4` to `4 5 2 1 3`.
