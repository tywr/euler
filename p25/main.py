import math

from utils.benchmark import benchmark


def log_fibonacci_binet_approximate(n):
    """
    Calculates the nth Fibonacci number using Binet's approximate formula.

    This method is fast for large n, but may suffer from floating-point
    precision issues for very large numbers.
    """
    if n < 0:
        return "Input must be a non-negative integer."

    phi = (1 + math.sqrt(5)) / 2

    # The formula returns a float, so we use round() to get the nearest integer.
    # The result is extremely close to the true integer value, so rounding works.
    return n * math.log10(phi) - 0.5 * math.log10(5)


@benchmark
def solve():
    """
    Approximate fibonacci number for great values of n
    """
    k = 0
    while 1:
        k += 1
        if log_fibonacci_binet_approximate(k) > 999:
            print(f"Fibonacci number for n={k} exceeds 1000 digits.")
            break


if __name__ == "__main__":
    solve()
