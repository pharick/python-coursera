# python-coursera

Solutions to the weekly programming exercises of an introductory Python 3 course on Coursera (the exercise set matches the MIPT "Programming in Python" course), March 2019. 203 scripts in nine weekly folders, one file per task; each reads from `input()` or `input.txt` and prints the answer, as the course's automatic grader expects.

## What it covers

| Folder | Topic |
|---|---|
| `week1` | `input`/`print`, integer arithmetic (`//`, `%`), digit extraction, clock and time-difference conversions |
| `week2` | conditionals and loops: max/min tracking, leap years, chessboard and box-comparison puzzles, Fibonacci, powers of two, reversing numbers, palindromes |
| `week3` | floats and `math`: quadratic equations and 2x2 linear systems, Horner's scheme, rounding, string slicing/replacement |
| `week4` | functions and recursion: gcd and fraction reduction, exponentiation by squaring, binomial coefficients, Towers of Hanoi, point-in-region tests |
| `week5` | lists: filtering, in-place reverse, cyclic shift, second maximum, run-length compression, "do any two queens attack" check |
| `week6` | sorting: merge of two sorted lists, counting sort, sorting by key with `namedtuple`, reading `input.txt` / writing `output.txt`, ranking problems |
| `week7` | sets and dicts: intersection/union of language sets, word frequencies, elections, phone-number normalisation, a bank-account simulator |
| `week8` | functional style: `lambda`, `map`/`zip`, `itertools.accumulate` and `permutations`, one-line solutions |
| `week9` | classes: a `Matrix` with `__add__`, `__mul__`/`__rmul__`, `__str__`, `transpose`, a `@staticmethod`, and a custom exception; driven by `exec(stdin.read())` as the grader requires |

## Notable exercises

- `week9/3-errors.py`: `Matrix` class with operator overloading, an in-place `transpose()` and a static `transposed()`, and a `MatrixError` that carries both operands when shapes do not match.
- `week7/22-accounts.py`: a bank simulator that reads `DEPOSIT`, `WITHDRAW`, `TRANSFER`, `INCOME` and `BALANCE` commands from a file and keeps balances in a dict, creating clients on first use.
- `week7/20-deputats.py`: proportional seat allocation (largest-remainder method) for 450 seats, with a two-key stable sort for the leftover seats.
- `week6/9-count-sort.py` and `week6/1-merge-lists.py`: counting sort and the merge step of merge sort written by hand.
- `week4/20-hanoi.py`: Towers of Hanoi in a four-line recursive `move`; `week4/13-fast-pow.py`: exponentiation by squaring including negative exponents.
- `week5/39-queens.py`: pairwise row / column / diagonal test over eight queen positions.

## Running

Python 3 only (keyword arguments to `print`, `input()`), no dependencies. Run a script and type its input:

```
python3 week4/20-hanoi.py
```

Eighteen scripts in `week6`-`week8` read `input.txt` from the current directory instead; `week6/8-sort-students.py` also writes `output.txt`.

## Notes

- Beginner-era code kept as a record: straightforward loops, no tests, some comments and identifiers in Russian. About 2 500 lines in 203 files.
