# USACO 2024 US Open Contest, Bronze: Problem 1 - Logical Moos

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=1419)

## Problem Description

Farmer John has a boolean statement that is N keywords long (1 ≤ N < 2·10⁵, N odd). Odd positions contain either "true" or "false", while even positions contain "and" or "or" operators.

A phrase "x OPERATOR y" evaluates as:
- "x and y": true if both x and y are true, false otherwise
- "x or y": true if either x or y is true, false otherwise

The statement follows operator precedence where "and" takes priority over "or". Evaluation proceeds by repeatedly selecting any "and" operation (if any exist) and replacing the surrounding phrase with its result. Once all "and" operations are resolved, the same process applies to "or" operations.

For Q queries, each specifying a range [l, r] and a target boolean value, determine if it's possible to replace that segment with a single boolean keyword such that the entire statement evaluates to the target value.

## Input Format

- Line 1: Two integers N and Q
- Line 2: N space-separated strings forming a valid boolean statement
- Next Q lines: Two integers l and r, and a string "true" or "false"

## Output Format

A string of length Q where the i-th character is "Y" if the i-th query is possible, otherwise "N".

## Sample Input 1

```
5 7
false and true or true
1 1 false
1 3 true
1 5 false
3 3 true
3 3 false
5 5 false
5 5 true
```

## Sample Output 1

```
NYYYNYY
```

## Sample Input 2

```
13 4
false or true and false and false and true or true and false
1 5 false
3 11 true
3 11 false
13 13 true
```

## Sample Output 2

```
YNYY
```
