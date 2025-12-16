# USACO 2019 January Contest, Bronze: Problem 3 - Guess the Animal

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=893)

## Problem Description

Bessie thinks of an animal, and Elsie asks yes/no questions about its characteristics to identify it. Elsie continues asking until only one animal remains in the "feasible set" (animals consistent with all answers so far).

Each question targets a characteristic of some animal currently in the feasible set. Elsie never asks the same characteristic twice.

The task is to determine the maximum number of "yes" answers Elsie could receive before identifying the correct animal.

## Input Format

- First line: integer N (2 ≤ N ≤ 100), the number of animals
- Next N lines: each describes an animal with format: `name K characteristic1 characteristic2 ... characteristicK`
  - K is between 1 and 100
  - Names and characteristics are lowercase strings (up to 20 characters)
  - No two animals share identical characteristic sets

## Output Format

Single integer: the maximum possible number of "yes" answers before the game ends.

## Sample Input

```
4
bird 2 flies eatsworms
cow 4 eatsgrass isawesome makesmilk goesmoo
sheep 1 eatsgrass
goat 2 makesmilk eatsgrass
```

## Sample Output

```
3
```
