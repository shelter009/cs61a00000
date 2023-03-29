import csv
import pickle
import math
import os
import json
from urllib.request import urlopen
with open('test.txt','at') as f:
    print("hhhh\n",file = f)
f = open('somefile','wb')
"""
pickle.dump(math.cos,f)
f.close()
f = open('somefile','rb')
print(pickle.load(f))
f.close()
"""

with open('test.csv',) as f:
    f_csv = csv.reader(f)
    #headers  = next(f_csv)
    for row in f_csv:
        print(tuple(row))

rows= [('112384', 'Apollo 13', '1995'),
('93779', 'The Princess Bride', '1987')]
"""
with open('test.csv','w') as f:
    f_csv = csv.writer(f)
    f_csv.writerows(rows)
"""

data = {
    'name': True,
    'shares': False,
    'prices': None
}
u = urlopen('https://api.github.com/users/')
resp = json.loads(u.read().decode('utf-8'))
from pprint import pprint
#json_str = json.dumps(data)
pprint(resp)