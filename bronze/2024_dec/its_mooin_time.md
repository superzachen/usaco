# USACO 2024 December Contest, Bronze: Problem 3 - It's Mooin' Time

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=1445)

## Problem Description

A "moo" is defined as a substring consisting of one character followed by two occurrences of a different character (pattern: cᵢ cⱼ cⱼ where cᵢ ≠ cⱼ). The task is to find all possible moos that appear at least F times in a given string, accounting for the possibility that up to one character in the string may have been corrupted during download.

## Input Format

- First line: two integers N and F, where N is the string length (3 ≤ N ≤ 20,000) and F is the frequency threshold (1 ≤ F ≤ N)
- Second line: a string of lowercase letters of length N

## Output Format

Print the count of valid moos, followed by each moo on a separate line in lexicographic order.

## Sample Input 1

```
10 2
zzmoozzmoo
```

## Sample Output 1

```
1
moo
```

## Sample Input 2

```
17 2
momoobaaaaaqqqcqq
```

## Sample Output 2

```
3
aqq
baa
cqq
```

## Sample Input 3

```
3 1
ooo
```

## Sample Output 3

```
25
aoo
boo
coo
doo
eoo
foo
goo
hoo
ioo
joo
koo
loo
moo
noo
poo
qoo
roo
soo
too
uoo
voo
woo
xoo
yoo
zoo
```
