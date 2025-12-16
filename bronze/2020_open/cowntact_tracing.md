# USACO 2020 US Open Contest, Bronze: Problem 3 - Cowntact Tracing

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=1037)

## Problem Description

Farmer John has N cows and discovered some are infected with COWVID-19. He has timestamped records of hoof-shake interactions between pairs of cows. The disease spreads under these rules:

- Exactly one cow ("patient zero") started with the disease
- An infected cow transmits the infection through her first K hoof shakes only
- After K shakes, she stops transmitting (through careful hygiene)
- Once infected, a cow remains infected

The task is to determine: how many cows could be patient zero, and what are the minimum and maximum possible values of K?

## Input Format

- Line 1: N (number of cows, 2 ≤ N ≤ 100) and T (number of interactions, 1 ≤ T ≤ 250)
- Line 2: String of N binary digits (0 = healthy, 1 = infected)
- Next T lines: Three integers t, x, y representing a hoof shake at time t between cows x and y

## Output Format

Three values: number of possible patient zeros, minimum K, maximum K (or "Infinity" if unbounded)

## Sample Input

```
4 3
1100
7 1 2
5 2 3
6 2 4
```

## Sample Output

```
1 1 Infinity
```

**Explanation:** Cow 1 is the only possible patient zero. For all K > 0, cow 1 infects cow 2 at time 7, while cows 3 and 4 remain uninfected, matching the final state.
