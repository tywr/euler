import math


def get_divisors(n):
    """
    Returns a sorted list of all divisors of a positive integer n.
    """
    if n <= 0:
        return []

    divs = set()
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divs.add(i)
            divs.add(n // i)

    return sorted(list(divs))
