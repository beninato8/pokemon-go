from pprint import pprint
import json

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

with open('master.json', 'r') as f:
    master = json.load(f)

d = master['itemTemplates']
t = []
for x in d:
    if 'pokemonSettings' in x.keys():
        t.append(x)

l = []
for x in t:
    if is_bad_name(x['templateId'].split('_')[2:]):
        # print(x['templateId'])
        continue
    stats = x['pokemonSettings']['stats']
    s = template_to_name(x['templateId'])
    l.append((s, stats, x['templateId']))
# pprint(l)

# exit()
stat_dict = {}
for (name, stats, ID) in l:
    stat_dict[name["name"]] = dict()
    stat_dict[name["name"]]["id"] = name["id"]
    stat_dict[name["name"]]["master_str"] = ID
    stat_dict[name["name"]]["attack"] = stats["baseAttack"]
    stat_dict[name["name"]]["defense"] = stats["baseDefense"]
    stat_dict[name["name"]]["stamina"] = stats["baseStamina"]
    # print(f'{name["name"]}:')
    # print(f'\tattack: {stats["baseAttack"]}')
    # print(f'\tdefense: {stats["baseDefense"]}')
    # print(f'\tstamina: {stats["baseStamina"]}')
    # print()

print(json.dumps(stat_dict))