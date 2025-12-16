# USACO 2020 February Contest, Bronze: Problem 2 - Mad Scientist

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=1012)

## Problem Description

Farmer John ordered N cows (1 ≤ N ≤ 1000) of two breeds: Holsteins (H) and Guernseys (G). He has a desired string A representing the order he wanted, but the actual delivery resulted in string B.

Ben's machine can toggle all breeds in any substring: H becomes G and G becomes H. The task is to find the minimum number of machine applications needed to transform B into A.

## Input Format

- Line 1: Integer N
- Line 2: String A (desired breed ordering)
- Line 3: String B (actual breed ordering)

Each string contains N characters that are either 'H' or 'G'.

## Output Format

Print the minimum number of times the machine must be applied to transform B into A.

## Sample Input

```
7
GHHHGHH
HHGGGHH
```

## Sample Output

```
2
```

## Explanation

Applying the machine to the first character transforms B to GHGGGHH. Then applying it to characters three and four produces the desired result A. Multiple two-operation combinations exist.
