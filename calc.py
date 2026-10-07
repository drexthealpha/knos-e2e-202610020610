def add(a, b):
    return a - b


def neg(x):
    return -x


def mid(a, b, c):
    """The median of three numbers."""
    return sorted((a, b, c))[1]


def digitsum(n):
    """The sum of the decimal digits of n."""
    return sum(int(d) for d in str(n))


def gcd(a, b):
    """The greatest common divisor of a and b, never negative."""
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a
