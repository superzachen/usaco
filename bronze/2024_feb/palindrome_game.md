# USACO 2024 February Contest, Bronze: Problem 1 - Palindrome Game

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=1395)

## Problem Description

Bessie and Elsie play a game starting with a pile of S stones (1 ≤ S < 10^(10^5)). Players alternate turns with Bessie going first. On each turn, a player must remove x stones, where x is a positive integer palindrome of their choice. A player who starts their turn with an empty pile loses.

A positive integer is a palindrome if it reads the same forward and backward (examples: 1, 121, 9009). Leading zeros are not permitted.

Both players play optimally. Determine the winner for each test case.

## Input Format

The first line contains T (1 ≤ T ≤ 10), the number of test cases. Each subsequent line contains a single integer S for that test case.

## Output Format

For each test case, output "B" if Bessie wins under optimal play, or "E" if Elsie wins.

## Sample Input

```
3
8
10
12
```

## Sample Output

```
B
E
B
```

## Explanation

- Test case 1: Bessie removes all 8 stones (a palindrome), winning immediately.
- Test case 2: 10 is not a palindrome, so Bessie cannot remove all stones. Elsie can always remove the remaining stones on her turn.
- Test case 3: Bessie wins under optimal play.
