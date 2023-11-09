def transpose(A: list[list[int]]) -> list[list[int]]:
    return list(zip(*A))


def determinant(A: list[list[int]]) -> int:
    a, b, c = A[0]
    d, e, f = A[1]
    g, h, i = A[2]

    return (a * e * i) + (b * f  * g) + (c * d * h) \
            - (g * e * c) - (h * f * a) - (i * d * b)


def multiplication(A: list[list[int]], B: list[list[int]]) -> list[list[int]]:
    return [
        [sum(a*b for a, b in zip(rowA, colB)) for colB in zip(*B)] for rowA in A
    ]
    # [a1, a2 a3]
    # [b1, b2 b3]
    # => [(a1, b1), (a2, b2), ...]
    # [a1*b1, a2*b2, ...]
    # a1 * b1 + a2 * b2 + ...
    # for all of the rows of A and for all columns of B
