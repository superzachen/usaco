# USACO 2025 January Contest, Bronze: Problem 1 - Astral Superposition

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=1467)

## Problem Description

Bessie uses a telescope to photograph an N×N grid of stars. Each star occupies exactly one pixel. Between two photos, every star either disappears or shifts A pixels right and B pixels down. Stars moving outside the frame or disappearing don't appear in the second photo.

Bessie accidentally superimposed the two photos, creating a composite where:
- **White pixels**: empty in both photos
- **Gray pixels**: star in exactly one photo
- **Black pixels**: star in both photos

"No new stars moved into the frame of the second photo, so her first photo contains all of the stars in the night sky."

Given the superimposed result, find the minimum number of initial stars. Output -1 if impossible.

**Constraints**: 1 ≤ N ≤ 1000; 0 ≤ A,B ≤ N; 1 ≤ T ≤ 1000

## Input Format

First line: T (number of test cases)

For each test case:
- First line: N A B
- Next N lines: N-character strings containing W, G, or B

## Output Format

For each test case, output the minimum number of initial stars, or -1 if impossible.

## Sample Input 1

```
1
3 0 0
WWB
BBB
GGG
```

## Sample Output 1

```
7
```

## Sample Input 2

```
3
5 1 2
GWGWW
WGWWW
WBWGW
WWWWW
WWGWW
3 1 1
WWW
WBW
WWW
3 1 0
GGB
GGW
WWW
```

## Sample Output 2

```
4
-1
4
```
