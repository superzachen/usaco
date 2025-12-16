# USACO 2021 February Contest, Bronze: Problem 1 - Year of the Cow

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=1107)

## Problem Description

Bessie the cow was born in a year of the Ox. The Chinese zodiac follows a 12-year cycle with these animals in order: "Ox, Tiger, Rabbit, Dragon, Snake, Horse, Goat, Monkey, Rooster, Dog, Pig, Rat, and then Ox again."

Elsie wants to know how many years apart she and Bessie were born. You must determine this by analyzing relationships between the birth years of several cows on the farm.

## Input Format

The first line contains an integer N (1 ≤ N ≤ 100). Each of the next N lines contains an 8-word phrase specifying the relationship between two cows' birth years.

Format: "[Cow1] born in [previous/next] [Animal] year from [Cow2]"

- First word: new cow name (not Bessie, not previously mentioned)
- 4th word: either "previous" or "next"
- 5th word: one of the 12 zodiac animals
- Last word: either "Bessie" or a previously mentioned cow name

"Previous" means the zodiac year strictly before the reference cow; "next" means strictly after.

## Output Format

Output a single integer representing the difference in years between Bessie and Elsie's birth years.

## Sample Input

```
4
Mildred born in previous Dragon year from Bessie
Gretta born in previous Monkey year from Mildred
Elsie born in next Ox year from Gretta
Paulina born in next Dog year from Bessie
```

## Sample Output

```
12
```
