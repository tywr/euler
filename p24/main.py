"""
There are 362,880 permutations starting with 0
There are 362,880 permutations starting with 1
The 1,000,000th permutation must therefore start with a 2
"""

import itertools
from utils.benchmark import benchmark


@benchmark
def solve():
    strings = [str(i) for i in [0, 1, 3, 4, 5, 6, 7, 8, 9]]
    permutation_iterator = itertools.permutations(strings)
    permutations = sorted(list(permutation_iterator))
    offset = 1_000_000 - 362_880 * 2 - 1
    result_list = ["2"] + list(permutations[offset])
    print("".join(result_list))


if __name__ == "__main__":
    solve()
