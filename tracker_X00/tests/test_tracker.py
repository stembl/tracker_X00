# tracker/tests/test_tracker.py

import numpy as np
# from ..print_gps import print_gps


def test_addition():
    actual = 1+1
    expected = 2
    assert actual == expected

    actual = 10 + 20
    expected = 30
    assert actual == expected


def test_tol():
    # Default values for tolerance: rtol = 1e-5, atol = 1e-8.
    actual = 0.123456789123
    expected = 0.12345678999
    assert np.allclose(actual, expected)
