#!python3

# convert mixed numbers to improper fractions
# convert improper fractions to mixed numbers of type a + b/c

def toImproper(a, b, c):
    fraction = [a * c + b, c]
    return tuple(fraction)


def toMixed(num, den):
    fraction = [num // den, num % den, den]
    return tuple(fraction)


if __name__ == "__main__":
    assert toMixed(10, 3) == (3, 1, 3)
    assert toMixed(3, 4) == (0, 3, 4)
    assert toMixed(9, 2) == (4, 1, 2)
    assert toImproper(5, 1, 3) == (16, 3)
    assert toImproper(2, 1, 2) == (5, 2)
