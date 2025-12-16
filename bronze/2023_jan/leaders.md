# USACO 2023 January Contest, Bronze: Problem 1 - Leaders

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=1275)

## Problem Description

Farmer John has N cows (2 ≤ N ≤ 10⁵), each with a breed that is either Guernsey or Holstein, standing in a line numbered 1 to N.

Each cow writes down a list of cows. Specifically, cow i's list contains the range of cows starting with herself (cow i) up to and including cow Eᵢ (i ≤ Eᵢ ≤ N).

FJ has recently discovered that each breed of cow has exactly one distinct leader. FJ does not know who the leaders are, but he knows that each leader must have a list that includes all the cows of their breed, or the other breed's leader (or both).

The task is to count valid leader pairs. A pair is valid if each cow's list either contains all cows of their breed or the other breed's leader (or both).

## Input Format

- Line 1: Integer N
- Line 2: String of length N where character i indicates breed (G for Guernsey, H for Holstein)
- Line 3: Space-separated values E₁ through Eₙ

## Output Format

Output the number of possible pairs of leaders.

## Sample Input 1

```
4
GHHG
2 4 3 4
```

## Sample Output 1

```
1
```

The only valid leader pair is (1, 2). Cow 1's list contains the other breed's leader (cow 2). Cow 2's list contains all cows of her breed.

## Sample Input 2

```
3
GGH
2 3 3
```

## Sample Output 2

```
2
```

Valid leader pairs are (1, 3) and (2, 3).
