import json
import ujson
import orjson
from time import time

"""
Check json vs ujson lib speed.
RESULT:
    - dumps:
        - ujson lib about 6,5x faster.
        - orjson lib about 42,5x faster. ## winner
    - loads:
        - ujson lib about 1,9x faster. ## winner
        - orjson lib about 1,5x faster.
"""

DATA_INNER = {"1": 1, "2": 2, "3": 3}
RANGE = 1000000

print("Creating dictionary of", "{:,.0f}".format(RANGE), "items")
DATA = {str(i): DATA_INNER for i in range(RANGE)}
print("Test 'dumps' STARTED")
#
start_1 = time()
json_val = json.dumps(DATA, indent=2)
end_1 = time()
start_2 = time()
ujson.dumps(DATA, indent=2)
end_2 = time()
start_3 = time()
orjson.dumps(DATA, option=orjson.OPT_INDENT_2)
end_3 = time()
#
print("dumps 'json': ", end_1 - start_1)
print("dumps 'ujson': ", end_2 - start_2)
print("dumps 'orjson': ", end_3 - start_3)
print("dumps ujson", round((end_1 - start_1)/(end_2 - start_2), 1), "x faster.")
print("dumps orjson", round((end_1 - start_1)/(end_3 - start_3), 1), "x faster.")
print()
print("Test 'loads' STARTED")
#
start_1 = time()
json.loads(json_val)
end_1 = time()
start_2 = time()
ujson.loads(json_val)
end_2 = time()
start_3 = time()
orjson.loads(json_val)
end_3 = time()
#
print("loads 'json': ", end_1 - start_1)
print("loads 'ujson': ", end_2 - start_2)
print("loads 'orjson': ", end_3 - start_3)
print("loads ujson", round((end_1 - start_1)/(end_2 - start_2), 1), "x faster.")
print("loads orjson", round((end_1 - start_1)/(end_3 - start_3), 1), "x faster.")
print("Test FINISHED")