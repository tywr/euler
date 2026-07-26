"""
Number letter counts
"""

LOOKUP = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
}


def map_integer_to_str(n: int, lookup: dict) -> int:
    if n < 0 or n > 1000:
        raise ValueError("Number should be between 0 & 1000.")
    elif n == 100:
        return "one hundred"
    elif n == 1000:
        return "one thousand"
    elif n in lookup:
        return lookup[n]
    else:
        s = ""
        hundreds = n // 100
        dozens = (n - hundreds * 100) // 10
        units = n % 10
        if hundreds > 0 and dozens == 0 and units == 0:
            s += lookup[hundreds] + " hundred"
        elif hundreds > 0:
            s += lookup[hundreds] + " hundred and "

        if dozens == 0 and units > 0:
            s += lookup[units]
        elif dozens > 0 and units == 0:
            s += lookup[dozens * 10]
        elif dozens == 1:
            s += lookup[dozens * 10 + units]
        elif dozens > 0 and units > 0:
            s += lookup[dozens * 10] + " " + lookup[units]
    return s


def solve(lookup: dict) -> int:
    total = 0
    for i in range(1, 1001):
        s =  map_integer_to_str(i, lookup)
        total += len(s.replace(" ", ""))
    return total


if __name__ == "__main__":
    print(solve(LOOKUP))
