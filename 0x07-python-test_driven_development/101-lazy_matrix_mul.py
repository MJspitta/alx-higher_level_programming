#!/usr/bin/python3
""" multiply 2 matrices using module NumPy """
import numpy as npy


def lazy_matrix_mul(m_a, m_b):
    """ function that multiplies 2 matrices by using
    the module NumPy """
    try:
        output = npy.matmul(m_a, m_b)
        return output
    except ValueError:
        raise ValueError("m_a and m_b can't be multiplied")
    except TypeError:
        raise TypeError("m_a must be a list of lists or m_b must be a list of lists")
    except (ValueError, TypeError):
        raise TypeError("m_a should contain only integers or floats or m_b should contain only integers or floats")
    except ValueError:
        raise ValueError("m_a can't be empty or m_b can't be empty")
    except TypeError:
        raise TypeError("m_a must be a list or m_b must be a list")
