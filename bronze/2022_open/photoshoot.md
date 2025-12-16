# USACO 2022 US Open Contest, Bronze: Problem 1 - Photoshoot

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=1227)

## Problem Description

Farmer John aims to arrange N cows (2 ≤ N ≤ 2×10⁵, N even) of two breeds—Guernseys (G) and Holsteins (H)—so that the maximum number of Guernseys occupy even-numbered positions. He can only manipulate the arrangement by reversing even-length prefixes of the cow line. The task is to find the minimum number of such reversals needed to achieve the optimal arrangement.

## Input Format

- Line 1: Integer N (the number of cows)
- Line 2: String of length N containing 'H' (Holstein) and 'G' (Guernsey) characters representing the initial cow ordering

## Output Format

Single integer: the minimum number of prefix reversals needed to maximize Guernseys in even positions

## Sample Input

```
14
GGGHGHHGHHHGHG
```

## Sample Output

```
1
```

## Explanation

Reversing the first six cows transforms the arrangement from having four Guernseys at even positions to six Guernseys at even positions, which is optimal. This is achieved with a single reversal operation.
