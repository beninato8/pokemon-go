import pandas as pd
from pprint import pprint
from datetime import datetime
import operator
import re

friends = pd.read_csv(f'friends.csv', names = ['time', 'name1', 'name2', 'code', 'area', 'team'])#.tail(1).values.tolist()[0][0]

d = dict()
f = friends.values.tolist()[1:]
# print(f)
p = r"[^\d]"

for x in f:
    if len(re.sub(p, "", x[3])) == 0:
        continue
    t = datetime.strptime(f'{x[0]}', '%m/%d/%Y %H:%M:%S').timestamp()
    if x[1] in d:
        if d[x[1]]['time'] > t:
            d[x[1]] = {'discord':x[2], 'code':x[3], 'time':t, 'area':x[4]}
    else:
            d[x[1]] = {'discord':x[2], 'code':x[3], 'time':t, 'area':x[4]}

l = []
for k,v in d.items():
    # print(k,v)
    c = str(int(re.sub(p, "", v['code'])))
    if len(c) < 12:
        c = (12-len(c))*"0"+str(c)
        # if 'isthmus' in v['area'].lower() and 'campus' not in v['area'].lower():
            # l.append((float(v['time']), f'{k}: {c}'))
        l.append((float(v['time']), f'{k}: {c}'))
    # exit()

for x in sorted(l, key=operator.itemgetter(0)):
    pass
# for x in l:
    print(datetime.utcfromtimestamp(int(x[0])).strftime('%d %b %Y'),end=' - ')
    print(x[1])

print(len(l))
