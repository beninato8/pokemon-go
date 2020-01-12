#!/usr/bin/env python3

import sys
import json
import re
from pprint import pprint
import os

from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def most_similar(s, names):
    l = []
    for name in names:
        l.append((similar(s.lower(), name.lower()), name))
    return sorted(l, reverse=True)[:5]

args = sys.argv
if len(args) < 2:
    print("Needs at least one argument")
    exit()

name = args[1]

with open(f'{os.path.dirname(os.path.abspath(__file__))}/game_masters/latest/latest.json', 'r') as f:
    gm = json.load(f)
pkm = dict()
for x in gm:
    if re.match(r'V\d{4}_POKEMON_.+', x['templateId']):
        num = int(x['templateId'].split('_')[0][1:])
        pkm[num] = x['pokemonSettings']['pokemonId']

if name.isdigit() and int(name) in pkm.keys():
    print(f'{pkm[int(name)].title()}: {name}')
    exit()

pkm = {v:k for k,v in pkm.items()}

sim_name = most_similar(name, pkm.keys())
for score, name in sim_name:
    print(f'{name.title()}: {pkm[name]}')