from math_series.series import fibonacci
from math_series.series import lucas


def test_import_fib():
    assert fibonacci


def test_import_lucas():
    assert lucas


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


def test_fib_10():
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
