# USACO 2018 February Contest, Bronze: Problem 1 - Teleportation

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=807)

## Problem Description

Farmer John needs to transport manure from location `a` to location `b` along a straight road. He has built a teleporter that connects two locations `x` and `y`, allowing instant transport between them. The challenge is to determine the minimum distance he must haul the manure by tractor, optionally using the teleporter if it reduces total distance.

## Input Format

A single line containing four space-separated integers: `a` and `b` (start and end locations), followed by `x` and `y` (the teleporter endpoints). All positions are integers in the range 0 to 100.

**File:** teleport.in

## Output Format

A single integer representing the minimum distance Farmer John needs to haul manure by tractor.

**File:** teleport.out

## Sample Input

```
3 10 8 2
```

## Sample Output

```
3
```

## Explanation

The optimal strategy hauls manure from position 3 to 2 (distance 1), teleports to position 8, then hauls to position 10 (distance 2), for a total tractor distance of 3.
