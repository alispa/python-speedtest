"""
Check what comparison is faster:
    - if not
    - OR if == 0
    - OR max(x - 1, 0) # if less than 0 return 0


RESULT:
    - method_2 is WINNER
    Details:
        - method_1 vs method_2 = 0.90x => WINNER: method_2
        - method_1 vs method_3 = 0.50x => WINNER: method_1
"""

from time import perf_counter
from random import shuffle

NR_ITEMS = 10_000_000
TEST_LIST = list((6, 4) for _ in range(NR_ITEMS))

# Convert the 3 different methods into separate functions
def method_1(group_list):
    for group in group_list:
        group_length = len(group)
        total = 0 if not group_length else (group_length - 1) * 5
    return total

def method_2(group_list):
    for group in group_list:
        group_length = len(group)
        total = 0 if group_length == 0 else ((group_length - 1) * 5)
    return total

def method_3(group_list):
    for group in group_list:
        group_length = len(group)
        total = max(group_length - 1, 0) * 5
    return total

methods = {1: method_1, 2: method_2, 3: method_3}

for _ in range(4):
    shuffled_keys = list(methods.keys())
    shuffle(shuffled_keys)

    results = {}
    for key in shuffled_keys:
        start = perf_counter()
        methods[key](TEST_LIST)
        end = perf_counter()
        duration = end - start
        results[f'r{key}'] = duration
        print(f"r{key}: {duration:.7f}")

    print(f"Difference r1/r2 {round(results['r1']/results['r2'], 1):,.2f}x")
    print(f"Difference r1/r3 {round(results['r1']/results['r3'], 1):,.2f}x")
    print()
