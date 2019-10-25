import json
import pandas as pd
import math


tiers = {4:list(range(0, 23)), 3:list(range(23, 30)), 2:list(range(30, 37)), 1:list(range(37, 46))}
def ivs(name, cp_num, highest=None, level=None, hp=None, tier=None):
    if level != None:
        lvlmax, lvlmin = level+1, level
    else:
        lvlmin, lvlmax = 1, 41
    for a in range(16):
        for d in range(16):
            for s in range(16):
                for lvl in range(lvlmin, lvlmax):
                    if cp(a, d, s, lvl, name) == cp_num:
                        if hp and hp_calc(s, name, lvl) != hp:
                            continue
                        if tier and sum((a,d,s)) not in tiers[tier]:
                            continue
                        string = f'{lvl} {ff(a, d, s)}'
                        if highest != None:
                            highest = set(highest)
                            if highest == {'a'} and a > d and a > s:
                                print(string)
                            if highest == {'d'} and d > a and d > s:
                                print(string)
                            if highest == {'s'} and s > d and s > a:
                                print(string)
                            if highest == {'s', 'a'} and s == a and s > d:
                                print(string)
                            if highest == {'s', 'd'} and s == d and s > a:
                                print(string)
                            if highest == {'a', 'd'} and a == d and a > s:
                                print(string)
                            if highest == {'a', 'd', 's'} and a == d and a == s:
                                print(string)
                        else:
                            print(string)

def mm(l):
    return (l[0], l[-1])

def ff(a, d, s):
    return f'{a}/{d}/{s} {round(sum((a,d,s))*100/45)}%'

class Combo:
    def __init__(self, a, d, s, lvl):
        self.a = a
        self.d = d
        self.s = s
        self.lvl = lvl

with open('simple.json', 'r') as f:
    stats = json.load(f)

data = pd.read_csv('cpm.csv').values.tolist()
cpm = {k:v for (k,v) in data}

def hp_calc(iv, name, level):
    base = stats[name]['stamina']
    return int(cpm[level] * (iv + base))

def cp(a, d, s, level, name):
    base = stats[name]
    attack = a + base['attack']
    defense = d + base['defense']
    stamina = s + base['stamina']
    return math.floor((attack * (defense**0.5) * (stamina**0.5) * (cpm[level]**2)) / 10)

l = []
for lvl in range(1, 35):
    for a in range(16):
        for d in range(16):
            for s in range(16):
                power = cp(a, d, s, lvl, "Blaziken")
                # power = cp(a, d, s, lvl, "Melmetal")
                if power < 1501 and power > 1450:
                    if power > 1499:
                        pass
                        # print(a, d, s, lvl)
                    l.append(Combo(a, d, s, lvl))

# print(l)
l2 = []
for x in l:
    # power = cp(x.a, x.d, x.s, x.lvl, "Meltan")
    power = cp(x.a, x.d, x.s, x.lvl, "Torchic")
    l2.append(power)
    # print(power)
# print(mm(sorted(set(l2))))
# print(cp(15, 15, 3, 19, "Blaziken"))
# print(cp(15, 15, 15, ))

for a in range(14, 16):
    for d in range(14, 16):
        for s in range(14, 16):
            for lvl in range(1, 35):
                power = cp(a, d, s, lvl, 'Torchic')
                # print(power, ff(a,d,s))
# print(stats['Sneasel'])
ivs('Shieldon', 654, highest=['d'], hp=79, tier=1)
# print(cp(13, 10, 15, 40, 'Bastiodon'))
# print(cp(15, 15, 15, 15, 'Zubat'))
# print(hp_calc(10, 'Rhyhorn', 31))