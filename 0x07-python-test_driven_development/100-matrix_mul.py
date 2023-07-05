#!/usr/bin/python3
""" multiply 2 matrices """


def matrix_mul(m_a, m_b):
    """ function that multiplies 2 matrices """
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list or m_b must be a list")
    if not all(isinstance(rw, list) for rw in m_a) or not all(isinstance(rw, list) for rw in m_b):
        raise TypeError("m_a must be a list of lists or m_b must be a list of lists")

    if len(m_a) == 0 or len(m_b) == 0:
        raise ValueError("m_a can't be empty or m_b can't be empty")
    if any(not all(isinstance(n, (int, float)) for n in rw) for rw in m_a) or \
            any(not all(isinstance(n, (int, float)) for n in rw) for rw in m_b):
                raise TypeError("m_a should contain only integers or floats or m_b should contain only integers or floats")

    if any(len(rw) != len(m_a[0]) for rw in m_a) or any(len(rw) != len(m_b[0]) for rw in m_b):
        raise TypeError("each row of m_a must be of the same size or each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    matrix_result = []
    for i in range(len(m_a)):
        rw = []
        for j in range(len(m_b[0])):
            value = sum(m_a[i][k] * m_b[k][j] for k in range(len(m_b)))
            rw.append(value)
        matrix_result.append(rw)

    return matrix_result
