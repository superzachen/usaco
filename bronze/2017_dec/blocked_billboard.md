# USACO 2017 December Contest, Bronze: Problem 1 - Blocked Billboard

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=759)

## Problem Description

Bessie observes two rectangular billboards from her barn window. A large rectangular truck parks across the street, potentially blocking her view. The task is to calculate the total visible area of both billboards after the truck potentially obscures portions of them. The two billboards don't overlap with each other.

## Input Format

Three lines of input, each containing four space-separated integers representing rectangle coordinates:
- Line 1: Lower-left and upper-right corners of the first billboard
- Line 2: Lower-left and upper-right corners of the second billboard
- Line 3: Lower-left and upper-right corners of the truck

All coordinates range from -1000 to +1000.

## Output Format

A single integer representing the total combined visible area of both billboards.

## Sample Input

```
1 2 3 5
6 0 10 4
2 1 8 3
```

## Sample Output

```
17
```

**Note:** The first billboard contributes 5 visible units and the second billboard contributes 12 visible units.
