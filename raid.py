import json
from pkm_types import fake_combo as effectivity
from pkm_types import types

t =['bug', 'dark', 'dragon', 'electric', 'fairy', 'fighting', 'fire', 'flying', 'ghost', 'grass', 'ground', 'ice', 'normal', 'poison', 'psychic', 'rock', 'steel', 'water']

print(types)
pokemon_types = ['water']

effective = []
for type1 in pokemon_types:
    for type2 in pokemon_types:
        if type1 == type2:
            effective = [k for k,v in effectivity([type1]).items() if v > 1]
        else:
            effective = [k for k,v in effectivity([type1, type2]).items() if v > 1]
        s1 = []
        s2 = []

        for x in effective:
            s1.append(f'@1{x}')
            s2.append(f'@2{x}')
            s2.append(f'@3{x}')

        print(','.join(s1)+'&'+','.join(s2))