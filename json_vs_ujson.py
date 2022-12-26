import json
import ujson
from time import time

"""
Check json vs ujson lib speed.
RESULT:
    - ujson lib about 6,5x faster.
"""

DATA_INNER = {"1": 1, "2": 2, "3": 3}
RANGE = 1000000

print("Creating dictionary of", "{:,.0f}".format(RANGE), "items")
DATA = {str(i): DATA_INNER for i in range(RANGE)}
print("Test STARTED")
#
start_1 = time()
json.dumps(DATA, indent=2)
end_1 = time()
start_2 = time()
ujson.dumps(DATA, indent=2)
end_2 = time()
#
print("lib 'json': ", end_1 - start_1)
print("lib 'ujson': ", end_2 - start_2)
print("lib ujson", round((end_1 - start_1)/(end_2 - start_2), 1), "x faster.")
print("Test FINISHED")
