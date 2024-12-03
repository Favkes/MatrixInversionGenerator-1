

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def lcm(a, b):
    return (a*b) // gcd(a, b)


class RealNumber:
    numerator: int
    denominator: int

    def __init__(self, num: int = 0, den: int = 1):
        self.numerator = num
        self.denominator = den

    def __mul__(self, other):
        self.numerator *= other.numerator
        self.denominator *= other.denominator
        return self

    def __truediv__(self, other):
        other.numerator, other.denominator = other.denominator, other.numerator
        return self * other

    def __add__(self, other):
        num1 = self.numerator
        den1 = self.denominator
        num2 = other.numerator
        den2 = other.denominator

        lcd = lcm(den1, den2)
        num1 *= lcd // den1
        num2 *= lcd // den2

        self.numerator = num1+num2
        self.denominator = lcd
        return self

    def __neg__(self):
        self.numerator = -self.numerator
        return self

    def __sub__(self, other):
        return self + (-other)

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'
