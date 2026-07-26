"""
Power digit sum
"""

def solve() -> int:
    num_str = str(2**1000)
    return sum(int(digit) for digit in num_str)


if __name__ == "__main__":
    print(solve())
