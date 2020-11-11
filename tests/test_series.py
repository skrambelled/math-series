from math_series.series import fibonacci
from math_series.series import lucas
from math_series.series import sum_series


def test_import_fib():
    assert fibonacci


def test_import_lucas():
    assert lucas


def test_import_sum_series():
    assert sum_series


def test_fib_0():
    actual = fibonacci(0)
    expect = 0
    assert actual == expect


def test_fib_1():
    actual = fibonacci(1)
    expect = 1
    assert actual == expect


def test_fib_3():
    actual = fibonacci(3)
    expect = 2
    assert actual == expect


def test_fib_6():
    actual = fibonacci(6)
    expect = 8
    assert actual == expect


def test_lucas_0():
    actual = lucas(0)
    expect = 2
    assert actual == expect


def test_lucas_1():
    actual = lucas(1)
    expect = 1
    assert actual == expect


def test_lucas_2():
    actual = lucas(2)
    expect = 3
    assert actual == expect


def test_lucas_3():
    actual = lucas(3)
    expect = 4
    assert actual == expect


def test_lucas_6():
    actual = lucas(6)
    expect = 18
    assert actual == expect


def test_sum_series_default_6():
    actual = sum_series(6)
    expect = 8
    assert actual == expect


def test_sum_series_fib_6():
    actual = sum_series(6, 0, 1)
    expect = 8
    assert actual == expect


def test_sum_series_lucas_0():
    # setting seed2 as some unreasonable value should not matter
    actual = sum_series(0, 2, 1000)
    expect = 2
    assert actual == expect


def test_sum_series_lucas_1():
    # setting seed1 as some unreasonable value should not matter
    actual = sum_series(1, 1000, 1)
    expect = 1
    assert actual == expect


def test_sum_series_lucas_2():
    actual = sum_series(2, 2, 1)
    expect = 3
    assert actual == expect


def test_sum_series_lucas_6():
    actual = sum_series(6, 2, 1)
    expect = 18
    assert actual == expect
