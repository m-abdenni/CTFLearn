# Chalkboard

## Description

* Solve the equations embedded in the jpeg to find the flag. Solve this problem before solving my Scope challenge which is worth 100 points.
* [Attachement](https://ctflearn.com/challenge/download/972)

## Solution

1. Running `exiftool`, we notice -in the comment section- that we get a half of the flag.
2. To get the other half, we need to solve the equation and replace 'x' and 'y' with their values

```
3x + 5y = 31
7x + 9y = 59
```

3. Solving the equation we find that: `x=2 ; y=5`

* Flag:

```
CTFlearn{I_Like_Math_2_5}
```