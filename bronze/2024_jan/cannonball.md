# USACO 2024 January Contest, Bronze: Problem 2 - Cannonball

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=1372)

## Problem Description

Bessie bounces along a number line of length N (1 ≤ N ≤ 10⁵) starting at position S with initial power 1, moving right. Each location contains either a target or jump pad with a value.

- **Jump pad** (q=0): Increases power by its value and reverses direction
- **Target** (q=1): Breaks if Bessie lands with power ≥ its value; doesn't affect power/direction
- Broken targets remain broken and can be bounced on again
- If Bessie starts on a breakable target, she breaks it immediately
- If on a jump pad at start, its effects apply before the first jump

Find how many targets Bessie breaks before leaving the number line or bouncing infinitely.

## Input Format

- Line 1: Two integers N and S (N = length, S = starting location)
- Lines 2 to N+1: Two integers qᵢ and vᵢ for each location i, where:
  - qᵢ = 0 for jump pad, qᵢ = 1 for target
  - vᵢ = value of location i (0 to N)

## Output Format

Output a single integer representing the count of targets broken.

## Sample Input 1

```
5 2
0 1
1 1
1 2
0 1
1 1
```

## Sample Output 1

```
1
```

## Sample Input 2

```
6 4
0 3
1 1
1 2
1 1
0 1
1 1
```

## Sample Output 2

```
3
```
