"""
Testing how much slower operations are on:
    1) float vs integer 
    2) integer of 1 digit vs 3 vs 10 digitis

RESULT:
    - float vs integer (float 1.5-1,7x slower)
    - 10 digit vs 1 digit (1.1-1.6x slower)
"""

import timeit


def test_1_digit():
    mylist = [2, 3, 4] * 1000
    for i in mylist:
        _ = i % 3 == 0


def test_3_digit():
    mylist = [200, 300, 400] * 1000
    for i in mylist:
        _ = i % 3 == 0


def test_10_digit():
    mylist = [2_000_000_000, 3_000_000_000, 4_000_000_000] * 1000
    for i in mylist:
        _ = i % 3 == 0


def test_float():
    mylist = [2.00, 3.00, 4.00] * 1000
    for i in mylist:
        _ = i % 3 == 0


time_1_digit = timeit.timeit(test_1_digit, number=1000)
time_3_digit = timeit.timeit(test_3_digit, number=1000)
time_10_digit = timeit.timeit(test_10_digit, number=1000)
time_float = timeit.timeit(test_float, number=1000)

print(f"1 digit: {time_1_digit:.4f} seconds")
print(f"3 digits: {time_3_digit:.4f} seconds")
print(f"10 digits: {time_10_digit:.4f} seconds")
print(f"Float: {time_float:.4f} seconds")
print(f"3/1: {time_3_digit/time_1_digit:.4f}x")
print(f"10/1: {time_10_digit/time_1_digit:.4f}x")
print(f"float/1: {time_float/time_1_digit:.4f}x")
