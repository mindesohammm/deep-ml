
def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    """
    Calculate the inverse of a 2x2 matrix.

    :param matrix: A 2x2 matrix
    :return: Inverse matrix or None if not invertible
    """
    a, b = matrix[0]
    c, d = matrix[1]

    det = (a * d) - (b * c)

    if det == 0:
        return None

    inverse = [
        [round(d / det, 3), round(-b / det, 3)],
        [round(-c / det, 3), round(a / det, 3)]
    ]

    return inverse