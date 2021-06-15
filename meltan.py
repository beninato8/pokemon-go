from stat_product import *

name = 'Meltan'
cps = set()
# print(f'{name}')
for lvl in range(1, 36): # 4*
    cps.add(cp(name, 15, 15, 15, lvl))
    cps.add(cp(name, 15, 15, 14, lvl))

gl = better_than('Melmetal', 3, 11, 15)
ul = better_than('Melmetal', 1, 14, 12, max_cp=2500)
for x in gl + ul:
    ivs, lvl = x.split(' ')
    a,d,s = map(int, ivs.split('/'))
    lvl = int(float(lvl)) + 1
    for l in range(1, lvl):
        cps.add(cp(name, a, d, s, l))

print('meltan&age0&!cp' + '&!cp'.join(map(str, sorted(cps))))