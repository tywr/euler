from utils.divisors import get_divisors
from sortedcontainers import SortedSet


def compute_abundant_numbers(limit: int = 28123) -> SortedSet[int]:
    abundant_numbers = SortedSet()

    for i in range(1, limit + 1):
        divisors = get_divisors(i)
        sum_divisors = sum(divisors) - i
        if sum_divisors > i:
            abundant_numbers.add(i)

    return abundant_numbers


def find_abundant_decomposition(
    n: int, abundant_numbers: SortedSet[int]
) -> tuple[int] | None:
    for k in abundant_numbers:
        # If we went past the n // 2 value, that means there is
        # no abundant decomposition
        if k > (n // 2 + 1):
            return None

        if (n - k) in abundant_numbers:
            return k, n - k


def solve():
    """
    Find the sum of all the positive integers which cannot be
    written as the sum of two abundant numbers.
    """
    total = 0
    limit = 28_123
    abundant_numbers = compute_abundant_numbers(limit=limit)
    for i in range(1, limit + 1):
        decomposition = find_abundant_decomposition(i, abundant_numbers)
        if decomposition is None:
            total += i
    return total


if __name__ == "__main__":
    total = solve()
    print("Answer:", total)
