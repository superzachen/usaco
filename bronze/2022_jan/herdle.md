# USACO 2022 January Contest, Bronze: Problem 1 - Herdle

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=1179)

## Problem Description

A puzzle game where players deduce a 3×3 grid of cow breeds (represented by letters A-Z) through guesses. Each guess receives feedback: green highlights indicate correct breed in the correct position, while yellow highlights indicate correct breed in the wrong position.

The key rule for yellow highlights: "if there are x cows of a certain breed in the guess grid and y < x cows of this breed in the answer grid (not counting cows in the right place that lead to green highlights), then only y of the x cows in the guess grid should be highlighted yellow."

## Input Format

Six lines of input: the first 3 lines represent the correct answer grid (a 3×3 grid of uppercase letters), and the next 3 lines represent the guess grid.

## Output Format

Two lines: first line contains the count of green highlights, second line contains the count of yellow highlights.

## Sample Input 1

```
COW
SAY
MOO
WIN
THE
IOI
```

## Sample Output 1

```
1
1
```

**Explanation:** The 'O' in position [2,2] matches (green). The 'W' exists in the answer but is misplaced (yellow).

## Sample Input 2

```
AAA
BBB
CCC
AYY
AAA
ZZZ
```

## Sample Output 2

```
1
2
```

**Explanation:** One 'A' is correctly placed (green). Two additional 'A's from the guess match the remaining 'A's in the answer but are misplaced (yellow).
