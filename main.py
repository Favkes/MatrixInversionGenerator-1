"""
    This project is a continuation to my already existing work on
    matrix inverses and generalizing the formulae for finding them.
    I have manually created a working equation matrix for finding
    inverses of 2x2 matrices, however even 3x3 have already proven
    too complex to be done by hand.
    Therefore this code will generate these huge equations automatically,
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


class ArithmeticalMatrix:
    unit_matrix: np.array
    body_matrix: np.array
    input_matrix: np.array

    def __init__(self, input_matrix: np.array):
        self.input_matrix = input_matrix
        self.body_matrix = gen_elements_matrix(input_matrix.shape[:2])
        self.unit_matrix = np.diag([1,] * input_matrix.shape[0])

    def __str__(self):
        y, x = self.input_matrix.shape
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


A = np.round(np.random.rand(2, 2) * 10)
I = np.diag([1,] * 2)

M = ArithmeticalMatrix(A)
print(M)
