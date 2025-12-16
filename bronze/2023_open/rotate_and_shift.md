# USACO 2023 US Open Contest, Bronze: Problem 3 - Rotate and Shift

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=1325)

## Problem Description

Farmer John's N cows stand in a circle and perform a coordinated dance. Initially, cow i occupies position i. Each minute, two simultaneous actions occur:

1. **Rotation**: Cows at "active" positions rotate cyclically—the cow at position A₁ moves to A₂, the cow at A₂ moves to A₃, and so forth, with the cow at A_K moving to A₁.

2. **Shift**: The active positions themselves increment by 1 (wrapping around from N-1 to 0).

The task is to determine the cow arrangement after T minutes of dancing.

## Input Format

- Line 1: Three integers N, K, and T
- Line 2: K integers representing the initial active positions A₁, A₂, ..., A_K (where A₁ = 0, in increasing order)

## Output Format

Display the cow order after T minutes, starting from position 0, with values separated by spaces.

## Sample Input

```
5 3 4
0 2 3
```

## Sample Output

```
1 2 3 4 0
```

## Example Trace

- T=0: order=[0 1 2 3 4], A=[0 2 3]
- T=1: order=[3 1 0 2 4], A=[1 3 4]
- T=2: order=[3 4 0 1 2], A=[2 4 0]
- T=3: order=[2 4 3 1 0], A=[3 0 1]
- T=4: order=[1 2 3 4 0], A=[4 1 2] (mod 5)
