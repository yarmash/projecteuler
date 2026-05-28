projecteuler
============

My working notebook of [Project Euler](https://projecteuler.net) solutions.

Most of the solutions are written in Python, with a smaller set of experiments
in Go, Perl, Scheme and others. The Python side is the main trail through the
problems: one file per puzzle, shared helpers where they are useful, and a few
tests for solutions whose details are easy to break while refactoring.

[![Project Euler profile](https://projecteuler.net/profile/doer.png)](https://projecteuler.net/profile/doer.png)

What is in here
---------------

- `python/` - the main collection, currently 100+ `pNNN.py` solutions.
- `python/utils.py` - shared number theory and combinatorics helpers.
- `python/tests/` - pytest/unittest coverage for selected solutions and helpers.
- `c/`, `go/`, `java/`, `perl/`, `scheme/` - alternate-language solutions and
  quick comparisons for a handful of problems.
- `data/` - input files used by Euler problems, such as matrices, words,
  poker hands, Sudoku grids, and cipher text.
- `doc/` - downloaded Project Euler overview PDFs for some solved problems.
- `answers` - known numeric answers, one per line, useful for quick checks.

Running Python solutions
------------------------

The Python project lives in `python/` and uses `uv` for its development
environment, but the solutions themselves are regular scripts. From the
`python/` directory, run one with Python:

```sh
cd python
python p001.py
```

Most files are also executable, so this works too:

```sh
./p001.py
```

Run the test suite from the same directory:

```sh
python -m unittest -v tests/*.py
```

For pytest, use the development environment:

```sh
uv run pytest
```

Why this exists
---------------

Project Euler is half math puzzle, half programming exercise. This repository
keeps the trail of both: direct brute-force scripts where that is the honest
solution, tighter number-theory code where the puzzle demands it, and the odd
alternate-language version when performance or curiosity makes that more fun.

The files are intentionally small and problem-shaped. If you are browsing, start
with the low-numbered Python files, then jump to anything with a data file or
test nearby; those tend to be the more interesting ones.
