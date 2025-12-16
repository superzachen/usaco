# USACO 2023 December Contest, Bronze: Problem 3 - Farmer John Actually Farms

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=1349)

## Problem Description

Farmer John is cultivating N plants with varying growth rates. Each plant i has an initial height of h_i inches and grows by a_i inches daily. FJ wants to arrange the plants so that plant i has exactly t_i other plants taller than it, where the t values form a permutation of 0 to N-1.

The task is to find the minimum number of days needed to satisfy these height requirements, or determine if it's impossible.

## Input Format

- First line: integer T (number of test cases, 1 ≤ T ≤ 10)
- For each test case:
  - Line 1: integer N
  - Line 2: N integers h_i (initial heights, 1 ≤ h_i ≤ 10^9)
  - Line 3: N integers a_i (daily growth rates, 1 ≤ a_i ≤ 10^9)
  - Line 4: N distinct integers t_i (desired ranking constraints)

## Output Format

Output T lines with the answer for each test case, or -1 if impossible.

## Sample Input 1

```
6
1
10
1
0
2
7 3
8 10
1 0
2
3 6
10 8
0 1
2
7 7
8 8
0 1
2
7 7
8 8
1 0
2
7 3
8 8
1 0
```

## Sample Output 1

```
0
3
2
5
-1
-1
```

## Sample Input 2

```
2
5
7 4 1 10 12
3 4 5 2 1
2 1 0 3 4
5
4 10 12 7 1
3 1 1 4 5
2 4 3 1 0
```

## Sample Output 2

```
4
7
```
