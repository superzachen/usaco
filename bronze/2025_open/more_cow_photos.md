# USACO 2025 US Open Contest, Bronze: Problem 2 - More Cow Photos

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=1516)

## Problem Description

The task involves arranging cows to create a photograph meeting specific constraints. Farmer John has N cows with distinct heights (1 to N) and wants to select and arrange a subset to form a valid photo.

The arrangement must satisfy three conditions:
- Heights must increase then decrease (forming a peak pattern)
- No two adjacent cows can have equal heights
- The arrangement must be symmetric (mirrored around the center)

The goal is to maximize the number of cows in the final arrangement.

## Input Format

- First line: integer T (number of test cases, 1 ≤ T ≤ 10⁵)
- For each test case:
  - First line: integer N
  - Second line: N space-separated integers representing cow heights (between 1 and N)

## Output Format

For each test case, output a single integer representing the maximum number of cows that can be included in a valid photo arrangement.

## Sample Input

```
2
4
1 1 2 3
4
3 3 2 1
```

## Sample Output

```
3
1
```

## Sample Explanation

**Test case 1:** Select cows with heights [1, 1, 3] and arrange as [1, 3, 1], satisfying all constraints.

**Test case 2:** Only a single cow with height 3 can form a valid arrangement.
