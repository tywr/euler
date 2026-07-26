"""
Longest Collatz Sequence solving
"""


def _count_sequence(n_start: int, lookup: dict = {}) -> int:
    """
    Returns the length of the collatz sequence when starting from
    n_start given a lookup. The function will also update the lookup
    once the value has been computed.
    """
    x, i = n_start, 0
    while x > 1:
        if x in lookup:
            lookup[n_start] = i + lookup[x]
            return i + lookup[x]
        if x % 2:
            x = 3 * x + 1
        else:
            x = x // 2
        i += 1

    lookup[n_start] = i
    return i


def solve(n_max=1_000_000) -> int:
    lookup = {}
    n_start, len_sequence = max(
        ((i, _count_sequence(i, lookup)) for i in range(n_max)), key=lambda x: x[1]
    )
    return n_start, len_sequence


if __name__ == "__main__":
    n_start, len_sequence = solve(n_max=1_000_000)
    print(
        "The starting number with the longest collatz sequence under "
        f"1'000'000 is {n_start} with a length of {len_sequence}"
    )
