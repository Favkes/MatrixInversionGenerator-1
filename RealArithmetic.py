

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def lcm(a, b):
    return (a*b) // gcd(a, b)


def sgn(a) -> int:
    """ Considers 0 as of sign=1. """
    return (-1)**(a <= 0)


class RealNumber:
    num: int    # numerator
    den: int    # denominator
    sgn: int    # sign

    def __init__(self, num: int = 0, den: int = 1):
        """ Class constructor. If you don't know what that is, *google it.* """
        self.num = num
        self.den = den
        self.sign_check()

    def sign_check(self):
        """ Ensures the sign is always stored in the numerator. """
        num = self.num
        den = self.den
        self.sgn = sgn(num) * sgn(den)

        self.num = abs(num) * self.sgn
        self.den = abs(den)

    def __mul__(self, other):
        return RealNumber(
            self.num*other.num,
            self.den*other.den
        )

    def __truediv__(self, other):
        return self * RealNumber(
            other.den,
            other.num
        )

    def __add__(self, other):
        num1 = self.num
        den1 = self.den
        num2 = other.num
        den2 = other.den

        lcd = lcm(den1, den2)
        num1 *= lcd // den1
        num2 *= lcd // den2

        return RealNumber(
            num1+num2,
            lcd
        )

    def __neg__(self):
        return RealNumber(
            -self.num,
            self.den
        )

    def __sub__(self, other):
        return self + (-other)

    def __str__(self):
        return f'{self.num}/{self.den}'

# a = RealNumber(2, 5)
# b = RealNumber(1, 5)
# print(a, b)
# print(a / b)