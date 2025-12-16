# USACO 2016 January Contest, Bronze: Problem 2 - Angry Cows

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=592)

## Problem Description

The player shoots a cow onto hay bales positioned on a number line. When a cow lands on a bale at position x, it explodes with "blast radius of 1, meaning that any other hay bales within 1 unit of distance are also engulfed by the explosion." Neighboring bales then explode simultaneously with blast radius 2, and this chain reaction continues with increasing blast radii. The objective is to determine the maximum number of hay bales that can be detonated by launching a single cow at an optimal starting position.

## Input Format

The first line contains N (1 ≤ N ≤ 100). The remaining N lines contain integers x₁...xₙ (each in the range 0...1,000,000,000), representing hay bale positions.

## Output Format

Output the maximum number of hay bales that can be caused to explode.

## Sample Input

```
6
8
5
6
13
3
4
```

## Sample Output

```
5
```

## Sample Explanation

Launching at position 5 detonates bales at positions 4 and 6 (blast radius 1). These explosions trigger bales at positions 3 and 8 (blast radius 2). The final explosions cannot reach the bale at position 13.
