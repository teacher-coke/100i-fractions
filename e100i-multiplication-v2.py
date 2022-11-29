#!python3

# Duplicate of d100i-multiplication.py
# except this should accept mixed numbers:

def product(f1,f2):
    # f1: tuple representing first fraction
        # a tuple with length 2 is a numerator/denominator 
        # a tuple with length 3 is a whole number/numerator/denominator
    # f2 is the same as 1
    
    return

if __name__ == "__main__":
    assert product((1,3),(4,1,2)) == (9,6)
    assert product( (3,4) , (5,3) ) == (15,12)
    assert product( (3,1,2) , (2,1,2) ) == (35,4)