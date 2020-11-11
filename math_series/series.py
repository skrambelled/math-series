def fibonacci(n):
    if(n == 0):
        return 0
    if(n == 1):
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


def lucas(n):
    if(n == 0):
        return 2
    if(n == 1):
        return 1
    return lucas(n-1) + lucas(n-2)


def sum_series(n, seed1=0, seed2=1):
    if(n == 0):
        return seed1
    if(n == 1):
        return seed2
    return sum_series(n-1, seed1, seed2) + sum_series(n-2, seed1, seed2)
