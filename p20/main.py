import math


def factorial_digit_sum(n):
    # First remove all trailing zeros from n
    numbers = [int(i) if i % 10 != 0 else i // 10 for i in range(2, n + 1)]
    product = math.prod(numbers)
    return sum(int(digit) for digit in str(product))


if __name__ == "__main__":
    print(factorial_digit_sum(100))
