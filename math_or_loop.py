"""
Comparing how much time can be save using math formulas over looping.
"""

import timeit

setup = """
items = list(range(1000000))  # Change range value for different list sizes
"""

code1 = """
total = sum(items) + len(items) * 3
"""

code2 = """
total = 0
for i in items:
    total += i + 3
"""

time1 = timeit.timeit(code1, setup, number=100)
time2 = timeit.timeit(code2, setup, number=100)

print(f"math: {time1:.5f} seconds")
print(f"For loop: {time2:.5f} seconds")
print(f"loop/math: {time2/time1:.5f}x")

