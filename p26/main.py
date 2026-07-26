from collections import defaultdict
from utils.benchmark import benchmark


def sieve_of_eratosthenes(n):
    """
    Finds all prime numbers up to n using the Sieve of Eratosthenes.
    """
    # Create a boolean array "is_prime" and initialize
    # all entries it as true. A number's index in the array is its value.
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers

    # Start from p = 2
    for p in range(2, int(n**0.5) + 1):
        # If is_prime[p] is not changed, then it is a prime
        if is_prime[p]:
            # Update all multiples of p
            for multiple in range(p * p, n + 1, p):
                is_prime[multiple] = False

    # Collect all prime numbers
    primes = []
    for num in range(n + 1):
        if is_prime[num]:
            primes.append(num)

    return primes


def get_cycle(n: int, d: int) -> list[int]:
    digits = []
    seen = {}
    while 1:
        q, r = divmod(n, d)
        digits.append(q)
        seen[(n, d)] = len(digits) - 1
        n, d = 10 * r, d
        if (n, d) in seen:
            cycle = digits[seen[(n, d)] :]
            return digits, cycle


@benchmark
def solve():
    longest_cycle, index = 0, 0
    primes = sieve_of_eratosthenes(1000)
    for i in primes:
        digits, cycle = get_cycle(1, i)
        if len(cycle) > longest_cycle:
            longest_cycle, index = len(cycle), i


if __name__ == "__main__":
    solve()
