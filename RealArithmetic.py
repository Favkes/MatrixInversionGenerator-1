

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

    def simplify(self):
        """ Converts the number into the simplest fraction possible. """
        divisor = gcd(abs(self.num), self.den)
        self.num //= divisor
        self.den //= divisor


    def __mul__(self, other):
        out = RealNumber(
            self.num*other.num,
            self.den*other.den
        )
        out.simplify()
        return out

    def __truediv__(self, other):
        out = self * RealNumber(
            other.den,
            other.num
        )
        out.simplify()
        return out

    def __add__(self, other):
        num1 = self.num
        den1 = self.den
        num2 = other.num
        den2 = other.den

        lcd = lcm(den1, den2)
        num1 *= lcd // den1
        num2 *= lcd // den2

        out = RealNumber(
            num1+num2,
            lcd
        )
        out.simplify()
        return out

    def __neg__(self):
        out = RealNumber(
            -self.num,
            self.den
        )
        out.simplify()
        return out

    def __sub__(self, other):
        out = self + (-other)
        out.simplify()
        return out

    def __str__(self):
        if self.num == 0:
            return '0'

        if self.den == 1:
            return str(self.num)

        return f'{self.num}/{self.den}'

# a = RealNumber(2, 5)
# b = RealNumber(1, 5)
# print(a, b)
# print(a / b)