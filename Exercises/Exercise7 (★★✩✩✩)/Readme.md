# Checksum (★★✩✩✩)
Create function calc_checksum(digits) that performs the following position-based calculation for the checksum of a number of any length given as a string, with the n digits modeled as z1 to zn:
```
z1z2z3 zn => (1*z + 2*z + 3*z + ... + n*zn)%10
```

## Examples
|Digits| Sum| Result|
|---|---|---|
|“11111”| 1 + 2 + 3 + 4 + 5 = 15| 15 % 10 = 5|
|“87654321”| 8 + 14 + 18 + 20 + 20 + 18 + 14 + 8 = 120| 120 % 10 = 0|