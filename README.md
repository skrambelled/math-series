# Math series module

Pull Request

## Problem Domain

For each series, find the n-th value of the given series

series | seed1 | seed2 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | etc
------ | ----- | ----- | - | - | - | - | - | - | - | - | ---
fibonacci(n) | 0 | 1 |0 | 1 | 1 | 2 | 3 | 5 | 8 | 13 | ...
lucas(n) | 2 | 1 | 2 | 1 | 3 | 4 | 7 | 11 | 18 | 29 | ...
sum_series(n, seed1, seed2) | 0 default | 1 default |

### Seeds

* For the Fibonacci series, 0 and 1 are the seeds
* For Lucas numbers, 2 and 1 are the seeds
* For sum_series, you can supply your own seeds, but if you do not it will default to the Fibonacci series seeds of 0 and 1

## Big O

O(2^n) - space and time, because we are calling this recursively for two values on each iteration.
