# USACO 2017 February Contest, Bronze: Problem 3 - Why Did the Cow Cross the Road III

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=713)

## Problem Description

Farmer John has built a fence around his farm with a single gate for entry. Cows must queue at the gate to answer security questions before entering. Each cow arrives at a specific time and requires a certain duration for questioning. Only one cow can be questioned at a time.

The task is to determine "the earliest possible time by which all cows are able to enter the farm."

## Input Format

The first line contains N (at most 100), the number of cows. Each subsequent line contains two positive integers (at most 1,000,000): arrival time and questioning duration for each cow.

## Output Format

A single integer representing the minimum time at which all cows complete processing.

## Sample Input

```
3
2 1
8 3
5 7
```

## Sample Output

```
15
```

## Sample Explanation

The first cow arrives at time 2 and takes 1 unit to process, finishing at time 3. The third cow arrives at time 5 and takes 7 units, finishing at time 12. The second cow arrives at time 8 but must wait until time 12, then takes 3 units to process, finishing at time 15.
