# USACO 2023 December Contest, Bronze: Problem 1 - Candy Cane Feast

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=1347)

## Problem Description

Farmer John has N cows with varying heights and M candy canes of different heights to distribute. The process works as follows:

- Candy canes are hung one at a time, suspended at ground level
- Cows line up in order and eat portions of the candy cane up to their current height
- The candy cane remains suspended and is not lowered as cows eat it
- After all cows feed on one candy cane, each cow grows by the amount they consumed
- The process repeats for each remaining candy cane

The candy cane's base position doesn't change, so a cow may eat nothing if the base is already above her height.

## Input Format

- Line 1: Two integers N and M (1 ≤ N, M ≤ 2×10⁵)
- Line 2: N integers representing initial cow heights (each in range [1, 10⁹])
- Line 3: M integers representing candy cane heights (each in range [1, 10⁹])

## Output Format

Output the final height of each cow on separate lines.

## Sample Input

```
3 2
3 2 5
6 1
```

## Sample Output

```
7
2
7
```

## Sample Walkthrough

For the first candy cane (height 6):
- Cow 1 (height 3) eats from 0-3, leaving candy cane at [3,6]
- Cow 2 (height 2) cannot reach the base at height 3, eats nothing
- Cow 3 (height 5) eats from 3-5, growing by 2

After round 1, cows are [6, 2, 7]. The second candy cane (height 1) is completely eaten by cow 1.
