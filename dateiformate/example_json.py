
import json

# wandle ein Dictionary in einen JSON-String um:
data = {'first': 1, 'second': 'two', 'third': [3,4,5]}
jj = json.dumps(data)
print(jj)

# wandle den JSON-String wieder in ein Dictionary um:
d = json.loads(jj)
print(d)
