from collections.abc import Sequence
from . import Random

#
# Adds a matrix class
# Used for math stuff.
#

# Multipling Rules
# x=y


class Matrix():  # 2d matrix
    """
    Creates A Matrix that can be used for many different math uses.

    :param MatrixValues:
        Sequence[Sequence[int]] - The values for the matrix (indexs y then x.)

    :raises ValueError:
        MatrixValues isn't a 2d int list
    """
    def __init__(self, MatrixValues: Sequence[Sequence[int]]):
        if not Random.RaisesError(
            "int(Matrix[0][0])",
            GlobalVars={"Matrix": MatrixValues}
        )[0]:
            raise ValueError("Matrix has to be a Sequence[Sequence[int]]")
        self.matrix = MatrixValues

    def __mul__(self, other):
        """
        Multiply two matrices
        """
        if not len(self.matrix[0]) == len(other.matrix):
            raise ValueError("X of first matrix needs to equal Y of second matrix.")
        elif not Random.RaisesError("int(Matrix.matrix[0][0])", GlobalVars={"Matrix": other})[0]:
            raise ValueError("Can only multiply a matrix by a matrix rn.")

        MatrixValues = [[0] * len(other.matrix[0])] * len(self.matrix)

        for index, i in enumerate(self.matrix):
            values = [0] * len(other.matrix[0])
            for idx, b in enumerate(i):
                for idx2, k in enumerate(other.matrix[idx]):
                    values[idx2] += int(b) * int(k)
            MatrixValues[index] = values

        return (Matrix(MatrixValues))

    def __str__(self):
        return str(self.matrix)
