import json
import re
import sys

f = open(sys.argv[1], "r")
tw_list = [
    re.search(
        '\w+ \w+ \d+',
        json.loads(line)['created_at']
    ).group(0) for line in f.readlines()
]
print(set(tw_list))

c = 0
f.seek(0)
for t in [json.loads(line) for line in f.readlines()]:
    if t['geo'] is not None:
        c += 1

print('geo count: %d' % c)
f.close()
