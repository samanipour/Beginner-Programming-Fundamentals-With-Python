## CH_Bonus2: Max Change Calculator 
Suppose you have a collection of coins or numbers of different values. Write function
calc_max_possible_change(values) that determines, for positive integers, what
amounts can be seamlessly generated with it starting from the value 1. The maximum
value should be returned as a result.

Examples

| Input | Possible values | Maximum |
| --- | --- | --- |
1|1|1
1, 1| 1, 2| 2
1, 5| 1| 1
1, 2, 4| 1, 2, 3, 4, 5, 6, 7| 7
1, 2, 3, 7| 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13| 13
1, 1, 1, 1, 5, 10, 20, 50| 1, 2, 3, 4, 5, 6, ... , 30, ... , 39|39