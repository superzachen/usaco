# USACO 2022 US Open Contest, Bronze: Problem 2 - Counting Liars

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=1228)

## Problem Description

Bessie the cow is hiding somewhere on the number line. Farmer John has N other cows, each of which provides information about Bessie's location.

Each cow makes a statement of one of two types:
- **L p**: Bessie is at a location less than or equal to p
- **G p**: Bessie is at a location greater than or equal to p

Unfortunately, not all cows necessarily tell the truth. Determine the minimum number of cows that must be lying for there to exist a valid hiding location for Bessie that is consistent with the statements of the remaining truthful cows.

## Input Format

- Line 1: A single integer N (1 ≤ N ≤ 1000)
- Lines 2..N+1: Each line contains either 'L' or 'G', followed by an integer p (0 ≤ p ≤ 10^9)

## Output Format

A single integer representing the minimum number of cows that must be lying.

## Sample Input 1

```
2
G 3
L 5
```

## Sample Output 1

```
0
```

No cow needs to be lying. Bessie could be hiding at location 3, 4, or 5.

## Sample Input 2

```
2
G 3
L 2
```

## Sample Output 2

```
1
```

At least one cow must be lying, since there's no location that is both ≥ 3 and ≤ 2.
