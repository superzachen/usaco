# USACO 2019 December Contest, Bronze: Problem 2 - Where Am I?

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=964)

## Problem Description

Farmer John is lost and hopes to determine his location by observing nearby mailboxes. Along a road there are N farms (1 ≤ N ≤ 100) arranged in a row, each with a colorful mailbox. Each mailbox color is represented by a letter A–Z.

Farmer John needs to find the smallest value of K such that any sequence of K consecutive mailboxes is unique and appears in only one location along the road. This way, observing any K consecutive mailboxes would uniquely identify his position.

For the example `ABCDABC`, the substring `ABC` appears twice (positions 0 and 4), so K=3 doesn't work. However, K=4 works because every 4-consecutive substring is unique along the road.

## Input Format

- Line 1: Integer N (the number of farms)
- Line 2: A string of N characters, each in the range A–Z

## Output Format

A single integer representing the smallest K value that uniquely identifies any position.

## Sample Input

```
7
ABCDABC
```

## Sample Output

```
4
```
