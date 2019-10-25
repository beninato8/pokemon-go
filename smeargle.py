import json
import re
from pprint import pprint
from operator import itemgetter
from tqdm import tqdm

with open('GAME_MASTER.json', 'r') as f:
    gm = json.load(f)

d = gm['itemTemplates']
pkm = [x for x in d if re.match(r'V\d{4}_POKEMON_.+', x['templateId'])]

def name(pkm):
    return re.sub(r'V\d{4}_POKEMON_', '', name)

pkm_moves = dict()

with open('names.json', 'r') as f:
    long_names = json.load(f)
def is_bad_name(name):
    name = '_'.join(name)
    return any(name in x for x in long_names.keys()) and name not in long_names

def exceptions(name):
    name = '_'.join(name)
    if name in long_names:
        name = ' '.join(long_names[name])
    return name.title()

def template_to_name(s):
    # print('')
    s = s.split('_')
    num = int(s[0][1:])
    name = s[2:]
    if len(name) > 0:
        name = exceptions(name)
        # print(name)
    # print(name)
    return {'name': name, 'id': num}

from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

names = dict()
for x in pkm:
    names[x['templateId']] = template_to_name(x['templateId'])['name']
name_to_id = {template_to_name(x['templateId'])['name']:template_to_name(x['templateId'])['id'] for x in pkm}
id_to_name = {template_to_name(x['templateId'])['id']:template_to_name(x['templateId'])['name'] for x in pkm}

def most_similar(elem , l):
    if '_FAST' in elem:
        elem = re.sub('_FAST', '', elem)
    elem = elem.title()
    simd = []
    for x in l:
        simd.append((similar(x, elem), x))
    return sorted(simd, key=itemgetter(0), reverse=True)[0][1]

moves = dict()
for x in pkm:
    moves[x['templateId']] = dict()
    try:
        moves[x['templateId']]['fast'] = x['pokemonSettings']['quickMoves']
    except Exception as e:
        moves[x['templateId']]['fast'] = []
    try:
        moves[x['templateId']]['charged'] = x['pokemonSettings']['cinematicMoves']
    except Exception as e:
        moves[x['templateId']]['charged'] = []

quickMoves = [x['combatMove']['uniqueId'] for x in d if re.match(r'COMBAT_V\d+_MOVE_.+_FAST$', x['templateId'])]
chargedMoves = [x['combatMove']['uniqueId'] for x in d if re.match(r'COMBAT_V\d+_MOVE_.+', x['templateId']) and x not in quickMoves]
quickMovesClean = {' '.join(x[:-5].split('_')).title():x for x in quickMoves}
chargedMovesClean = {' '.join(x.split('_')).title():x for x in chargedMoves}

# pprint(moves)
def get_pkm_with_moves(fast, charged):
    oldfast = fast
    oldcharged = charged
    print(most_similar(fast, quickMovesClean), '/', most_similar(charged, chargedMovesClean))
    fast = quickMovesClean[most_similar(fast, quickMovesClean)]
    charged = chargedMovesClean[most_similar(charged, chargedMovesClean)]
    l = set()
    for k,v in moves.items():
        if fast in v['fast'] and charged in v['charged']:
            l.add(name_to_id[names[k]])

    # print(len(l))
    # if len(l) == 16:
        # print(f'fast: {fast}, charged: {charged}, {oldfast}, {oldcharged}')
    return l


l = []
b = True
b = False
if b:
    # for quick in quickMoves:
    for quick in tqdm(quickMoves):
        for charge in chargedMoves:
            pkm = get_pkm_with_moves(quick, charge)
            size = len(pkm)
            # if pkm and size >= 16:
                # print(quick, charge, size, pkm)
            if size > 0:
                l.append((size, f'{quick}, {charge}'))
    pprint(sorted(l))




# pprint(get_pkm_with_moves('zen headbutt', 'psychic'))

pprint([id_to_name[x] for x in get_pkm_with_moves('spark', 'wild charge')])




"""
 (10, 'BUG_BITE_FAST, BUG_BUZZ'),
 (10, 'BUG_BITE_FAST, STRUGGLE'),
 (10, 'BUG_BITE_FAST, STRUGGLE_BUG_FAST'),
 (10, 'HEX_FAST, SHADOW_BALL'),
 (10, 'ROCK_THROW_FAST, ROCK_SLIDE'),
 (10, 'SPARK_FAST, DISCHARGE'),
 (10, 'TACKLE_FAST, THUNDERBOLT'),
 (10, 'WING_ATTACK_FAST, AERIAL_ACE'),
 (11, 'BUBBLE_FAST, WATER_PULSE'),
 (11, 'CHARGE_BEAM_FAST, ZAP_CANNON'),
 (11, 'CONFUSION_FAST, FUTURESIGHT'),
 (11, 'CONFUSION_FAST, PSYBEAM'),
 (11, 'CONFUSION_FAST, PSYSHOCK'),
 (11, 'MUD_SLAP_FAST, EARTHQUAKE'),
 (11, 'QUICK_ATTACK_FAST, AERIAL_ACE'),
 (12, 'FEINT_ATTACK_FAST, FOUL_PLAY'),
 (12, 'RAZOR_LEAF_FAST, SOLAR_BEAM'),
 (12, 'TACKLE_FAST, DIG'),
 (12, 'THUNDER_SHOCK_FAST, THUNDERBOLT'),
 (12, 'WATER_GUN_FAST, ICE_BEAM'),
 (12, 'ZEN_HEADBUTT_FAST, PSYCHIC'),
 (13, 'AIR_SLASH_FAST, AERIAL_ACE'),
 (13, 'EMBER_FAST, FLAME_CHARGE'),
 (13, 'TACKLE_FAST, BODY_SLAM'),
 (14, 'WATER_GUN_FAST, HYDRO_PUMP'),
 (15, 'SPARK_FAST, THUNDERBOLT'),
 (17, 'BUBBLE_FAST, BUBBLE_BEAM'),
 (17, 'BUBBLE_FAST, BUBBLE_FAST'),
 (17, 'EMBER_FAST, FLAMETHROWER'),
 (21, 'WATER_GUN_FAST, WATER_PULSE'),
 (26, 'BITE_FAST, CRUNCH'),
 (31, 'CONFUSION_FAST, PSYCHIC')]
 """