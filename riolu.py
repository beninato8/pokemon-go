import pandas as pd
import math

class Combo:
    def __init__(self, a, d, s, lvl):
        self.a = a
        self.d = d
        self.s = s
        self.lvl = lvl

data = pd.read_csv('cpm.csv').values.tolist()
cpm = {k:v for (k,v) in data}
# print(cpm)
def stat(individual, base, lvl):
    return (individual + base)

baseA = 236
baseD = 144
baseS = 172

def cp(a, d, s, level):
    attack = stat(baseA, a, level)
    defense = stat(baseD, d, level)
    stamina = stat(baseS, s, level)
    return math.floor((attack * (defense**0.5) * (stamina**0.5) * (cpm[level]**2)) / 10)


combos = []
for a in range(0, 16):
    # break
    for d in range(0, 16):
        for s in range(0, 16):
            for lvl in range(20, 24):
                string = f'{a}/{d}/{s} {round((a+d+s)*100/45)}% LVL{lvl}'
                n = cp(a, d, s, lvl)
                if n < 1501:
                    combos.append(Combo(a, d, s, lvl))

baseA = 127
baseD = 78
baseS = 120
cps = []
for x in combos:
    cps.append(cp(x.a, x.d, x.s, x.lvl))

t = sorted(set(cps))
for x in t:
    print(x)
# print(cp(7,15,15,20))