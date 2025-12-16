# USACO 2023 US Open Contest, Bronze: Problem 2 - Moo Language

[Problem Link](https://usaco.org/index.php?page=viewproblem2&cpid=1324)

## Problem Description

Farmer John wants to learn the moo language, which has four word types: nouns, transitive verbs, intransitive verbs, and conjunctions. Valid sentence structures are:

- **Type 1:** noun + intransitive verb.
- **Type 2:** noun + transitive verb + noun(s), where commas precede all but the first following noun.

Two sentences can be joined with a conjunction to form a compound sentence (which cannot be further joined). All sentences must end with periods.

Given N words, C commas, and P periods, the task is to output a sequence using the maximum possible number of words.

## Input Format

- First line: T (number of test cases)
- For each test case:
  - First line: N, C, P (word count, comma count, period count)
  - Next N lines: word and type (noun, transitive-verb, intransitive-verb, or conjunction)

## Output Format

- Line 1: Maximum number of words
- Line 2: A valid sequence achieving this maximum (careful with whitespace)

## Sample Input 1

```
1
1 1 1
bessie noun
```

## Sample Output 1

```
0

```

## Sample Input 2

```
1
10 5 4
bessie noun
john noun
farmer noun
elsie noun
and conjunction
flew intransitive-verb
nhoj noun
taught transitive-verb
mooed intransitive-verb
cow noun
```

## Sample Output 2

```
9
nhoj mooed. farmer taught elsie, bessie and john flew.
```

## Sample Input 3

```
1
24 5 4
bessie noun
john noun
farmer noun
elsie noun
and conjunction
but conjunction
flew intransitive-verb
nhoj noun
pushed transitive-verb
mooed intransitive-verb
cow noun
bob noun
impressed transitive-verb
envy noun
bella noun
buttercup noun
leaped intransitive-verb
cud noun
ate transitive-verb
grass noun
mooloo noun
milked transitive-verb
mooooo intransitive-verb
ambled intransitive-verb
```

## Sample Output 3

```
23
nhoj mooed. nhoj impressed john, farmer, elsie, bessie and cow impressed bob. bella pushed elsie and buttercup flew. envy mooed but john leaped.
```
