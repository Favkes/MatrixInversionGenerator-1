"""
    This project is a continuation to my already existing work on
    matrix inverses and generalizing the formulae for finding them.
    I have manually created a working equation matrix for finding
    inverses of 2x2 matrices, however even 3x3 have already proven
    too complex to be done by hand.
    Therefore, this code will generate these huge equations automatically,
    and potentially simplify them as well.
"""
import numpy as np


def gen_elements_matrix(dims: tuple[int, int]):
    y, x = dims
    lst = [None] * x * y
    i = 0
    for y_ in range(y):
        for x_ in range(x):
            lst[i] = f'a_{y_}_{x_}'
            i += 1
    arr = np.array(lst, dtype=object)
    arr = np.reshape(arr, (y, x))
    return arr


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


class ArithmeticalMatrix:
    dims: tuple[int, int]
    unit_matrix: np.array
    body_matrix: np.array
    input_matrix: np.array

    def __init__(self, input_matrix: np.array):
        self.dims = input_matrix.shape[:2]
        self.input_matrix = input_matrix
        self.body_matrix = gen_elements_matrix(input_matrix.shape[:2])
        self.unit_matrix = np.diag([1,] * input_matrix.shape[0])

    def alpha(self):
        """Gaussian elimination part of the algorithm."""
        y, x = self.dims
        A = self.input_matrix
        for y_ in range(1, y):
            psi = A[y_, 0] / A[0, 0]
            for x_ in range(x):
                A[y_, x_] = A[y_, x_] - A[0, x_] * psi


    def __str__(self):
        y, x = self.dims
        inM = self.input_matrix
        bdM = self.body_matrix
        unM = self.unit_matrix
        s = ''
        for y_ in range(y):
            inS = bdS = unS = ''
            for x_ in range(x):
                inS += f'{inM[y_, x_]}, '
                bdS += f'{bdM[y_, x_]}, '
                unS += f'{unM[y_, x_]}, '
            s += f'[{inS[:-2]} | {unS[:-2]} | {bdS[:-2]}]\n'
        return s


A = np.round(np.random.rand(3, 3) * 10)
I = np.diag([1,] * 2)

M = ArithmeticalMatrix(A)
# print(M)

M.alpha()
# print(M)

