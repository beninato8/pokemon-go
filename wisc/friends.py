import pandas as pd
from pprint import pprint
from datetime import datetime
import operator

friends = pd.read_csv(f'friends.csv', names = ['time', 'name1', 'name2', 'code', 'area', 'team'])#.tail(1).values.tolist()[0][0]

d = dict()
f = friends.values.tolist()[1:]
# print(f)
for x in f:
    if isinstance(x[-2], str):
        if 'campus' in x[-2].lower():
            t = datetime.strptime(f'{x[0]}', '%m/%d/%Y %H:%M:%S').timestamp()
            if x[1] in d:
                if d[x[1]]['time'] < t:
                    d[x[1]] = {'discord':x[2], 'code':x[3], 'time':t}
            else:
                d[x[1]] = {'discord':x[2], 'code':x[3], 'time':t}

l = []
for k,v in d.items():
    l.append((float(v['time']), f'{k}: {int(v["code"].replace(" ", "").replace("-", ""))}'))

for x in sorted(l, key=operator.itemgetter(0))[::-1]:
# for x in l:
    print(x[1])

print(len(l))
