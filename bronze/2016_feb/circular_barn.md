# USACO 2016 February Contest, Bronze: Problem 2 - Circular Barn

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=616)

## Problem Description

Farmer John built a circular barn with n rooms arranged in a ring (numbered 1 to n clockwise). Each room connects to its two neighbors and has an exterior door. The farmer wants exactly rᵢ cows in room i and plans to unlock one exterior door to let cows enter. Cows walk clockwise until reaching their destination. The goal is to find which door minimizes total walking distance, where distance equals the number of interior doors traversed.

## Input Format

The first line contains n (where 3 ≤ n ≤ 1,000). The next n lines contain r₁ through rₙ, where 1 ≤ rᵢ ≤ 100 for each room.

## Output Format

Output the minimum total distance all cows must collectively walk.

## Sample Input

```
5
4
7
8
6
4
```

## Sample Output

```
48
```

## Explanation

The optimal solution is to unlock the exterior door for the room requiring 7 cows.
