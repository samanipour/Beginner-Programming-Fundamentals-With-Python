# Prime Number Pairs (★★✩✩✩)
Compute all pairs of prime numbers with a distance of 2 (twin), 4 (cousin), and 6 (relative) up to an upper bound for n. For twins then the following is true:
```
is _Prime(n)&&is _Prime (n + 2)
```

## Examples
The following results are expected for limit 50:
|Type| Result|
|---|---|
|twin| {3: 5, 5: 7, 11: 13, 17: 19, 29: 31, 41: 43}|
|cousin| {3: 7, 7: 11, 13: 17, 19: 23, 37: 41, 43: 47}|
|relative| {5: 11, 7: 13, 11: 17, 13: 19, 17: 23, 23: 29, 31: 37, 37: 43, 41: 47, 47: 53}|