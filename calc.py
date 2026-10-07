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


def cube(x):
    """x to the third power."""
    return x * x * x
