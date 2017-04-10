class Rational:
    def __init__(self, x, y):
        numer = x
        if y == 0:
            raise ZeroDivisionError()
        else:
            denominator = y
try:
    rational1 = Rational(4, 1)
    rational2 = Rational(3, 0)
except:
    print("Cannot have a rational number with 0 as denominator")
