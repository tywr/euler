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


def sum_proper_divisors(n):
    """
    Returns the sum of all proper divisors of a positive integer n.
    Proper divisors are all divisors excluding the number itself.
    """
    if n <= 0:
        return 0

    divs = get_divisors(n)
    return sum(divs) - n


def get_amicable_pairs(n):
    d = {}
    for i in range(n):
        d[i] = sum_proper_divisors(i)

    pairs = set()
    for n, v in d.items():
        if v in d and d[v] == n and n != v:
            pairs.add((min(n, v), max(n, v)))
    return pairs


if __name__ == "__main__":
    pairs = get_amicable_pairs(10_000)
    total = 0
    for v1, v2 in pairs:
        total += (v1 + v2)
    print(total)


