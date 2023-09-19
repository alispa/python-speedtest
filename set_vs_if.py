"""
This script compares the performance of two approaches for identifying unique items in a list and populating a dictionary with those unique items.

The list `TEST_LIST` is populated with a repeated sequence of characters. Two methods are then used to find unique items and populate the `res` dictionary:
1. Directly iterating over the list and checking the dictionary for existence (which can be slow for large lists).
2. Converting the list to a set (to get unique values) and then iterating over the set to populate the dictionary.

The performance of each method is timed using `perf_counter` and the results are printed. It's demonstrated that the set-based approach is significantly faster, especially for large lists.

Attributes:
    _nr_items (int): Number of times each character is repeated in the test list.
    _test_chars (list of str): List of characters to be repeated in the test list.
    TEST_LIST (list of str): The actual test list populated with repeated characters.
    res (dict): Dictionary populated with unique items from TEST_LIST as keys.

"""

from time import perf_counter

_nr_items = 10_000_000
_test_chars = ["a", "b", "c", "d", "e"]
TEST_LIST = [char for char in _test_chars for _ in range(_nr_items)]

res = dict()

# Run through a list and check
start = perf_counter()
for i in TEST_LIST:
    if i in res:
        continue
    res[i] = None
end = perf_counter()
r1 = end - start
print(r1)

# First make a set (unique values) and then check
start = perf_counter()
test_set = set(TEST_LIST)
for i in test_set:
    if i in res:
        continue
    res[i] = None
end = perf_counter()
r2 = end - start
print(r2)

# Set solution is expected to be much faster (about 5x)
print(f"Difference list/set {round(r1/r2, 1)}x")
