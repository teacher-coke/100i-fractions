#!python3

# Duplicate of d100i-multiplication.py
# except this should accept mixed numbers:

def product(f1, f2):
    if len(f1) == 2 and len(f2) == 2:
        fraction = [f1[0] * f2[0], f1[1] * f2[1]]
        return tuple(fraction)
    elif len(f1) == 3 and len(f2) == 3:
        fraction1 = [f1[0] * f1[2] + f1[1], f1[2]]
        fraction2 = [f2[0] * f2[2] + f2[1], f2[2]]
        fraction = [fraction1[0] * fraction2[0], fraction1[1] * fraction2[1]]
        return tuple(fraction)
    elif len(f1) == 2 and len(f2) == 3:
        fraction1 = [f2[0] * f2[2] + f2[1], f2[2]]
        fraction = [f1[0] * fraction1[0], fraction1[1] * f1[1]]
        return tuple(fraction)
    elif len(f2) == 2 and len(f1) == 3:
        fraction1 = [f1[0] * f1[2] + f1[1], f1[2]]
        fraction = [f2[0] * fraction1[0], fraction1[1] * f2[1]]
        return tuple(fraction)
    # f1: tuple representing first fraction
    # a tuple with length 2 is a numerator/denominator
    # a tuple with length 3 is a whole number/numerator/denominator
    # f2 is the same as 1


if __name__ == "__main__":
    assert product((1, 3), (4, 1, 2)) == (9, 6)
    assert product((3, 4), (5, 3)) == (15, 12)
    assert product((3, 1, 2), (2, 1, 2)) == (35, 4)
