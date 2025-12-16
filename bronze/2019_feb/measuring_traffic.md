# USACO 2019 February Contest, Bronze: Problem 3 - Measuring Traffic

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=917)

## Problem Description

Farmer John has installed sensors along a highway to measure traffic flow. Each sensor produces a range of possible values rather than exact readings. The highway spans N miles, and sensors are placed on one-mile segments. Some segments have on-ramps (where traffic enters), off-ramps (where traffic exits), or neither.

The goal is to determine the most specific possible ranges for: (1) traffic flow rate before mile 1, and (2) traffic flow rate after mile N, such that all sensor readings are consistent.

## Input Format

- First line: integer N (1 ≤ N ≤ 100)
- Next N lines: each contains a string ("on", "off", or "none") followed by two integers (0 to 1000) representing the lower and upper bounds of the sensor reading
- At least one segment will have "none"

## Output Format

- Line 1: two integers representing the range [lower, upper] for traffic flow before mile 1
- Line 2: two integers representing the range [lower, upper] for traffic flow after mile N

## Sample Input

```
4
on 1 1
none 10 14
none 11 15
off 2 3
```

## Sample Output

```
10 13
8 12
```
