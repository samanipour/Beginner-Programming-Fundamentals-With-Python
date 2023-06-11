# Roman Numbers ➤ Decimal Numbers (★★★✩✩)

Write function from_roman_number(roman_number) that computes the corresponding decimal number from a textually valid Roman number.

## Examples

| Arabic | Roman     |
| ------ | --------- |
| 17     | “XVII”    |
| 444    | “CDXLIV”  |
| 1971   | “MCMLXXI” |
| 2020   | “MMXX”    |

## Roman Numbers Rules

The Roman numeral system works with special letters and combinations of them to represent numbers. The following basic mapping is applicable:
|Roman number| I |V |X |L |C |D |M|
|---|---|---|---|---|---|---|---|
|Value| 1 |5 |10 |50 |100 |500 |1000 |

The corresponding value is usually calculated by adding the values of the individual digits from left to right. Normally (see the following rules), the largest number is on the left and the smallest number is on the right, for example, XVI for the value 16.

## Rules

Roman numerals are composed according to certain rules:

1. Addition rule: The same digits next to each other are added, for example XXX = 30. Likewise, this applies to smaller digits after larger ones, so XII = 12.
2. Repetition rule: No more than three identical digits may follow
each other. According to rule 1, you could write the number 4 as
IIII, which this rule 2 forbids. This is where the subtraction rule
comes into play.
3. Subtraction rule: If a smaller number symbol appears in front of a
larger one, the corresponding value is subtracted. Let’s look again
at 4. It can be represented as subtraction 5 − 1. This is expressed
as IV in the Roman numeral system. The following rules apply to
the subtraction:
- I precedes only V and X.
- X precedes only L and C.
- C precedes only D and M.
