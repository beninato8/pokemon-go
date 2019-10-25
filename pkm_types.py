import json
from pprint import pprint
import operator

with open('types.json', 'r') as f:
    effectivity = json.load(f)

# pprint(effectivity)

categories = {1:"normal",
              1.6:"weak to",
              0.625:"resistant to",
              0.390625:"very resistant to",
              2.56:"very weak to",
              0.244141:"extremely resistant to"
}
types = ["bug", "dark", "dragon",
         "electric", "fairy", "fighting",
         "fire", "flying", "ghost", "grass",
         "ground", "ice", "normal", "poison",
         "psychic", "rock", "steel", "water"]

def fake_combo(pkm):
    stats = {}
    for p in types:
        stats[p] = round(effectivity[p][pkm[0]], 6)
    for i in range(1, len(pkm)):
        for p in types:
            stats[p] = round(effectivity[p][pkm[i]] * stats[p], 6)
    return dict(sorted(stats.items(), key=operator.itemgetter(1), reverse = True))
    return stats

def do_thing(pokemon):
    stats = {}

    for p in types:
        stats[p] = round(effectivity[p][pokemon[0]], 6)

    if len(pokemon) == 2:
        for p in types:
            stats[p] = round(effectivity[p][pokemon[1]] * stats[p], 6)


    stats = {k:categories[v] for (k,v) in sorted(stats.items(), key=operator.itemgetter(1)) if v != 1}
    # print(stats)

    # name = '/'.join(pokemon)
    # print(f'{name} is ')
    return stats
    for k,v in stats.items():
        pass
        # print(f'\t{v} {k} attacks')
    return sum([1 for v in stats.values() if 'weak' in v])

# count = {}
# for x in types:
#     for y in types:
#         if x == y:
#             count[x] = do_thing([x])
#         else:
#             count[f'{x} {y}'] = do_thing([x, y])
# print({k:v for (k,v) in sorted(count.items(), key=operator.itemgetter(1))})
if __name__ == '__main__':
    print(fake_combo(['water', 'fighting' , 'poison']))
