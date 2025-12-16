# USACO 2025 January Contest, Bronze: Problem 3 - Cow Checkups

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=1469)

## Problem Description

Farmer John has N cows in a line, each of species aᵢ. A veterinarian will check cow at position i only if its species matches bᵢ. FJ will perform exactly one operation: reverse the cows between positions l and r (inclusive). The task is to count, for each possible number of checked cows c (from 0 to N), how many distinct operations (l,r) result in exactly c cows being checked.

## Input Format

- Line 1: Integer N
- Line 2: Species of each cow: a₁, a₂, ..., aₙ
- Line 3: Required species at each position: b₁, b₂, ..., bₙ

## Output Format

N+1 lines, where line i contains the count of operations resulting in exactly i-1 checked cows.

## Sample Input 1

```
3
1 3 2
3 2 1
```

## Sample Output 1

```
3
3
0
0
```

## Sample Input 2

```
3
1 2 3
1 2 3
```

## Sample Output 2

```
0
3
0
3
```

## Sample Input 3

```
7
1 3 2 2 1 3 2
3 2 2 1 2 3 1
```

## Sample Output 3

```
0
6
14
6
2
0
0
0
```
