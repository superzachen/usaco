# USACO 2015 US Open Contest, Bronze: Problem 2 - Bessie Gets Even

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=546)

## Problem Description

Farmer John receives a mathematical expression from Bessie: (B+E+S+S+I+E)(G+O+E+S)(M+O+O) with seven variables. Each variable has a list of possible integer values (ranging from -300 to 300). The task is to count how many different variable assignments make the entire expression evaluate to an even number.

## Input Format

- First line: integer N (number of variable-value pairs)
- Next N lines: each contains a variable name and one possible value for that variable
- Each variable appears 1-20 times; no duplicate values per variable

## Output Format

A single integer representing the count of valid assignments producing an even result.

## Sample Input

```
10
B 2
E 5
S 7
I 10
O 16
M 19
B 3
G 1
I 9
M 2
```

## Sample Output

```
6
```

## Explanation

Six assignments yield even results:
- (B,E,S,I,G,O,M) = (2,5,7,10,1,16,19) → 53,244
- (2,5,7,10,1,16,2) → 35,496
- (2,5,7,9,1,16,2) → 34,510
- (3,5,7,10,1,16,2) → 36,482
- (3,5,7,9,1,16,19) → 53,244
- (3,5,7,9,1,16,2) → 35,496

Different variable assignments count separately even if they produce identical values.
