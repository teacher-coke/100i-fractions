#!python3

# program to add 2 fractions
# return the sum of the 2 fractions as a tuple with numerator and
# denominator in the lowest terms
def sum(n1, d1, n2, d2):
    n1 *= d2
    n2 *= d1
    d1 *= d2
    n3 = n1 + n2
    fraction = [n3, d1]
    if n3 == d1:
        return 1, 1
    else:
        for i in range(1, d1):
            if n3 % i == 0 and d1 % i == 0:
                fraction[0] = n3 / i
                fraction[1] = d1 / i
    return tuple(fraction)


if __name__ == "__main__":
    assert sum(1, 3, 2, 1) == (7, 3)
    assert sum(1, 4, 3, 4) == (1, 1)
    assert sum(5, 2, 3, 5) == (31, 10)
