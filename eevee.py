from stat_product import *
from operator import itemgetter
from tqdm import tqdm
import json

eeveelutions = ["Vaporeon", "Jolteon", "Flareon", "Espeon", "Umbreon", "Leafeon", "Glaceon"]
eeveelutions = ["Glaceon"]

with open('eevee.txt', 'r') as f:
    ivs = f.read().split('\n')
ivs = [[int(y) for y in x.split(' ')] for x in ivs if len(x) > 0]

# products = dict()
# for evo in tqdm(eeveelutions):
#     products[evo] = []
#     for a in range(0,16):
#         for d in range(0,16):
#             for s in range(0,16):
#                 lvl = max_lvl(evo, a=a, d=d, s=s)
#                 products[evo].append(product(evo, a, d, s))
#     products[evo] = sorted(products[evo], reverse=True)

# with open('eevee.json', 'w+') as f:
#     json.dump(products, f, indent=2)

with open('eevee.json', 'r') as f:
    products = json.load(f)

for a,d,s in ivs:
    print(f'{a}/{d}/{s}')
    ranks = []
    for evo in eeveelutions:
        rank = 1 + min([products[evo].index(x) for x in products[evo] if x == product(evo, a, d, s)])
        ranks.append((rank, f'   L{max_lvl(evo, a=a, d=d, s=s)} {evo}: Rank {rank}'))
    for x in sorted(ranks, key=itemgetter(0)):
        print(x[1])