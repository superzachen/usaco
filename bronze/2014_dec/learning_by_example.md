# USACO 2014 December Contest, Bronze: Problem 4 - Learning by Example

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=490)

## Problem Description

Farmer John is building a nearest neighbor classifier to predict whether incoming cows will have spots based on data from his existing herd. For each new cow with weight in range [A, B], the classifier finds the existing cow with the closest weight. If that nearest neighbor has spots, the new cow is classified as spotted; if no unique nearest neighbor exists (tie), the new cow is classified as spotted if at least one tied cow has spots.

## Input Format

- First line: Three integers N, A, and B (1 ≤ N ≤ 50,000; 1 ≤ A ≤ B ≤ 1,000,000,000)
- Next N lines: Each contains either "S W" (spotted cow) or "NS W" (non-spotted cow), where W is the weight (1 to 1,000,000,000)
- All existing cow weights are distinct

## Output Format

A single integer representing how many incoming cows (with weights A through B inclusive) will be classified as having spots.

## Sample Input

```
3 1 10
S 10
NS 4
S 1
```

## Sample Output

```
6
```

## Explanation

The incoming cows with weights 1, 2, 7, 8, 9, and 10 are classified as spotted, totaling 6 cows. Note: The solution must handle the large range efficiently rather than iterating through each weight individually.
