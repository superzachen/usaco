# USACO 2015 December Contest, Bronze: Problem 2 - Speeding Ticket

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=568)

## Problem Description

Bessie has stolen a tractor and driven 100 miles down a road. A police officer issued her a speeding ticket, which Bessie wants to contest. The task is to determine the maximum speed Bessie exceeded the limit by during any portion of her journey.

The road consists of N segments, each with a specified length and speed limit. Bessie's journey consists of M segments, each with a specified length and driving speed. Both the road and journey total exactly 100 miles.

## Input Format

- First line: Two integers N and M (number of road segments and journey segments)
- Next N lines: Two integers each—segment length (miles) and speed limit (mph, range 1-100)
- Next M lines: Two integers each—segment length (miles) and Bessie's speed (mph, max 100)

## Output Format

A single integer representing the maximum amount by which Bessie exceeded the speed limit at any point. Output 0 if she never exceeds the limit.

## Sample Input

```
3 3
40 75
50 35
10 45
40 76
20 30
40 40
```

## Sample Output

```
5
```

## Sample Explanation

The road has three segments (40 miles at 75 mph, 50 miles at 35 mph, 10 miles at 45 mph). Bessie drives three segments (40 miles at 76 mph, 20 miles at 30 mph, 40 miles at 40 mph). During her last segment, she exceeds the speed limit by 5 mph at its worst point, giving the answer of 5.
