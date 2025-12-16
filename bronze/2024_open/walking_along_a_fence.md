# USACO 2024 US Open Contest, Bronze: Problem 2 - Walking Along a Fence

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=1420)

## Problem Description

Farmer John has N cows that walk daily around a fence enclosing a pasture. The fence consists of P posts forming a rectilinear polygon (sides parallel to axes). Each cow has a starting and ending position on the fence and will walk in the shorter direction around the fence's closed loop.

## Input Format

- First line: N (number of cows) and P (number of posts)
- Next P lines: Two integers (x, y) representing post coordinates in order
- Next N lines: Four integers x₁ y₁ x₂ y₂ representing each cow's start and end positions

## Output Format

N integers, each representing the distance walked by each cow (choosing the shorter of two possible routes)

## Sample Input

```
5 4
0 0
2 0
2 2
0 2
0 0 0 2
0 2 1 0
2 1 0 2
1 0 1 2
1 2 1 0
```

## Sample Output

```
2
3
3
4
4
```
