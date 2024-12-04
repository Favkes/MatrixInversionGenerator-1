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
import RealArithmetic as re


def gen_elements_matrix(dims: tuple[int, int]):
    """ Generates a matrix of arithmetical element variables. """
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


def matrix_int2real(matrix):
    """ Converts a matrix of dtype int to dtype RealNumber """
    lst = []
    for row in matrix:
        for element in row:
            lst.append(re.RealNumber(int(element)))
    matrix = np.reshape(np.array(lst, dtype=object), matrix.shape[:2])
    return matrix


class ArithmeticalMatrix:
    dims: tuple[int, int]
    unit_matrix: np.array
    body_matrix: np.array
    input_matrix: np.array

    def __init__(self, input_matrix: np.array):
        self.dims = input_matrix.shape[:2]

        self.input_matrix = matrix_int2real(
            input_matrix
        )
        self.unit_matrix = matrix_int2real(
            np.diag([1,] * input_matrix.shape[0])
        )

        self.body_matrix = gen_elements_matrix(input_matrix.shape[:2])

    def alpha(self):
        """Gaussian elimination method - part 1. of the algorithm."""
        y, x = self.dims
        A = self.input_matrix
        B = self.unit_matrix

        for y_ in range(1, y):
            psi = A[y_, 0] / A[0, 0]
            for x_ in range(x):
                A[y_, x_] = A[y_, x_] - A[0, x_] * psi
                B[y_, x_] = B[y_, x_] - B[0, x_] * psi


    def __str__(self):
        y, x = self.dims
        inM = self.input_matrix
        unM = self.unit_matrix
        bdM = self.body_matrix


        def prepare_columns(matrix):
            out = [[''] * x for _ in range(y)]
            for x_ in range(x - 1):
                for y_ in range(y):
                    out[x_][y_] = f'{matrix[y_, x_]}, '
            for y_ in range(y):
                out[-1][y_] = f'{matrix[y_, -1]}'
            return out

        inCol = prepare_columns(inM)
        unCol = prepare_columns(unM)
        bdCol = prepare_columns(bdM)

        def prepare_rows(prepared_columns):
            out = ['']*y
            for col in prepared_columns:
                lenCol = [i for i in map(len, col)]
                largest = max(lenCol)

                for row in range(y):
                    out[row] += col[row] + ' '*(largest-lenCol[row])
            return out

        in_s = prepare_rows(inCol)
        un_s = prepare_rows(unCol)
        bd_s = prepare_rows(bdCol)

        glued = zip(in_s, un_s, bd_s)

        S = ''
        for row in glued:
            S += f'[ {row[0]} | {row[1]} | {row[2]} ]\n'

        return S


A = np.round(np.random.rand(3, 3) * 10)

M = ArithmeticalMatrix(A)
print(M)

# M.alpha()
# print(M)

