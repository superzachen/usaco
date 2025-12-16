# USACO 2017 December Contest, Bronze: Problem 2 - The Bovine Shuffle

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=760)

## Problem Description

Farmer John teaches his N cows (1 ≤ N ≤ 100) a dance called the "Bovine Shuffle." The cows perform three consecutive shuffles, where each shuffle is defined by a permutation that moves the cow at position i to position aᵢ. Given the final arrangement of cows after all three shuffles, determine their initial order. Each cow has a unique 7-digit ID number.

## Input Format

- Line 1: Integer N (number of cows)
- Line 2: N integers a₁...aₙ (shuffle permutation)
- Line 3: N integers representing cow IDs in their order after three shuffles

## Output Format

N lines, each containing a single cow ID, specifying the initial arrangement before shuffles.

## Sample Input

```
5
1 3 4 5 2
1234567 2222222 3333333 4444444 5555555
```

## Sample Output

```
1234567
5555555
2222222
3333333
4444444
```
