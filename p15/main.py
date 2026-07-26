"""
Lattice paths problem

The grid is 20x20 and we want to find the number of unique paths to
go to the bottom right corner. In any case we'll have to do 20
movements to the right, and 20 movements down. In total, we'll
make 40 movements that can be either right or down.

            R > ...
        R >
    R >
R >     R > ...
    D >
        D >
            D > ...


There are in total 2^40 combinations of strings like "RDRDRDRD...RD" of length 40.
We are only interested in the strings that have exactly 20 times the letter R.
This is exactly the binomial coefficient comb(40, 20) !
"""
from math import comb


def solve() -> int:
    return comb(40, 20)


if __name__ == "__main__":
    print(solve())
