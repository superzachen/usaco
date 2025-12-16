# USACO 2017 January Contest, Bronze: Problem 1 - Don't Be Last!

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=687)

## Problem Description

Farmer John tracks milk production for 7 cows: Bessie, Elsie, Daisy, Gertie, Annabelle, Maggie, and Henrietta. The task is to identify which cow produces the second-smallest total amount of milk. Cows absent from the log are assumed to have produced zero milk.

## Input Format

- First line: integer N (1 ≤ N ≤ 100) - number of log entries
- Following N lines: cow name followed by a positive integer (at most 100) representing milk produced in one session

## Output Format

Output the name of the cow with the second-smallest total milk production. Specifically, if M is the minimum production across all cows, output the cow producing the minimal amount greater than M. If multiple cows tie for this position or all cows produce equal amounts, output "Tie".

## Sample Input

```
10
Bessie 1
Maggie 13
Elsie 3
Elsie 4
Henrietta 4
Gertie 12
Daisy 7
Annabelle 10
Bessie 6
Henrietta 5
```

## Sample Output

```
Henrietta
```

## Explanation

Bessie, Elsie, and Daisy tie for minimum production at 7 units each. Henrietta's total of 9 units represents the next-largest production level.
