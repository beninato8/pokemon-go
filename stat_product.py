import json
import pandas as pd
import math
import operator
from pprint import pprint

ALL_NAMES = "Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon", "Charizard", "Squirtle", "Wartortle", "Blastoise", "Caterpie", "Metapod", "Butterfree", "Weedle", "Kakuna", "Beedrill", "Pidgey", "Pidgeotto", "Pidgeot", "Alolan Rattata", "Rattata", "Alolan Raticate", "Raticate", "Spearow", "Fearow", "Ekans", "Arbok", "Pikachu", "Alolan Raichu", "Raichu", "Alolan Sandshrew", "Sandshrew", "Alolan Sandslash", "Sandslash", "Nidoran", "Nidorina", "Nidoqueen", "Nidorino", "Nidoking", "Clefairy", "Clefable", "Alolan Vulpix", "Vulpix", "Alolan Ninetales", "Ninetales", "Jigglypuff", "Wigglytuff", "Zubat", "Golbat", "Oddish", "Gloom", "Vileplume", "Paras", "Parasect", "Venonat", "Venomoth", "Alolan Diglett", "Diglett", "Alolan Dugtrio", "Dugtrio", "Alolan Meowth", "Meowth", "Alolan Persian", "Persian", "Psyduck", "Golduck", "Mankey", "Primeape", "Growlithe", "Arcanine", "Poliwag", "Poliwhirl", "Poliwrath", "Abra", "Kadabra", "Alakazam", "Machop", "Machoke", "Machamp", "Bellsprout", "Weepinbell", "Victreebel", "Tentacool", "Tentacruel", "Alolan Geodude", "Geodude", "Alolan Graveler", "Graveler", "Alolan Golem", "Golem", "Ponyta", "Rapidash", "Slowpoke", "Slowbro", "Magnemite", "Magneton", "Farfetchd", "Doduo", "Dodrio", "Seel", "Dewgong", "Alolan Grimer", "Grimer", "Alolan Muk", "Muk", "Shellder", "Cloyster", "Gastly", "Haunter", "Gengar", "Onix", "Drowzee", "Hypno", "Krabby", "Kingler", "Voltorb", "Electrode", "Exeggcute", "Alolan Exeggutor", "Exeggutor", "Cubone", "Alolan Marowak", "Marowak", "Hitmonlee", "Hitmonchan", "Lickitung", "Koffing", "Weezing", "Rhyhorn", "Rhydon", "Chansey", "Tangela", "Kangaskhan", "Horsea", "Seadra", "Goldeen", "Seaking", "Staryu", "Starmie", "Mr Mime", "Scyther", "Jynx", "Electabuzz", "Magmar", "Pinsir", "Tauros", "Magikarp", "Gyarados", "Lapras", "Ditto", "Eevee", "Vaporeon", "Jolteon", "Flareon", "Omanyte", "Omastar", "Kabuto", "Kabutops", "Aerodactyl", "Snorlax", "Articuno", "Zapdos", "Moltres", "Dratini", "Dragonair", "Dragonite", "Mewtwo", "Mew", "Chikorita", "Bayleef", "Meganium", "Cyndaquil", "Quilava", "Typhlosion", "Totodile", "Croconaw", "Feraligatr", "Sentret", "Furret", "Hoothoot", "Noctowl", "Ledyba", "Ledian", "Spinarak", "Ariados", "Crobat", "Chinchou", "Lanturn", "Pichu", "Cleffa", "Igglybuff", "Togepi", "Togetic", "Natu", "Xatu", "Mareep", "Flaaffy", "Ampharos", "Bellossom", "Marill", "Azumarill", "Sudowoodo", "Politoed", "Hoppip", "Skiploom", "Jumpluff", "Aipom", "Sunkern", "Sunflora", "Yanma", "Wooper", "Quagsire", "Espeon", "Umbreon", "Murkrow", "Slowking", "Misdreavus", "Unown", "Wobbuffet", "Girafarig", "Pineco", "Forretress", "Dunsparce", "Gligar", "Steelix", "Snubbull", "Granbull", "Qwilfish", "Scizor", "Shuckle", "Heracross", "Sneasel", "Teddiursa", "Ursaring", "Slugma", "Magcargo", "Swinub", "Piloswine", "Corsola", "Remoraid", "Octillery", "Delibird", "Mantine", "Skarmory", "Houndour", "Houndoom", "Kingdra", "Phanpy", "Donphan", "Porygon2", "Stantler", "Smeargle", "Tyrogue", "Hitmontop", "Smoochum", "Elekid", "Magby", "Miltank", "Blissey", "Raikou", "Entei", "Suicune", "Larvitar", "Pupitar", "Tyranitar", "Lugia", "Ho Oh", "Celebi", "Treecko", "Grovyle", "Sceptile", "Torchic", "Combusken", "Blaziken", "Mudkip", "Marshtomp", "Swampert", "Poochyena", "Mightyena", "Zigzagoon", "Linoone", "Wurmple", "Silcoon", "Beautifly", "Cascoon", "Dustox", "Lotad", "Lombre", "Ludicolo", "Seedot", "Nuzleaf", "Shiftry", "Taillow", "Swellow", "Wingull", "Pelipper", "Ralts", "Kirlia", "Gardevoir", "Surskit", "Masquerain", "Shroomish", "Breloom", "Slakoth", "Vigoroth", "Slaking", "Nincada", "Ninjask", "Shedinja", "Whismur", "Loudred", "Exploud", "Makuhita", "Hariyama", "Azurill", "Nosepass", "Skitty", "Delcatty", "Sableye", "Mawile", "Aron", "Lairon", "Aggron", "Meditite", "Medicham", "Electrike", "Manectric", "Plusle", "Minun", "Volbeat", "Illumise", "Roselia", "Gulpin", "Swalot", "Carvanha", "Sharpedo", "Wailmer", "Wailord", "Numel", "Camerupt", "Torkoal", "Spoink", "Grumpig", "Spinda", "Trapinch", "Vibrava", "Flygon", "Cacnea", "Cacturne", "Swablu", "Altaria", "Zangoose", "Seviper", "Lunatone", "Solrock", "Barboach", "Whiscash", "Corphish", "Crawdaunt", "Baltoy", "Claydol", "Lileep", "Cradily", "Anorith", "Armaldo", "Feebas", "Milotic", "Castform", "Rainy Castform", "Snowy Castform", "Sunny Castform", "Kecleon", "Shuppet", "Banette", "Duskull", "Dusclops", "Tropius", "Chimecho", "Absol", "Wynaut", "Snorunt", "Glalie", "Spheal", "Sealeo", "Walrein", "Clamperl", "Huntail", "Gorebyss", "Relicanth", "Luvdisc", "Bagon", "Shelgon", "Salamence", "Beldum", "Metang", "Metagross", "Regirock", "Regice", "Registeel", "Latias", "Latios", "Kyogre", "Groudon", "Rayquaza", "Jirachi", "Attack Forme Deoxys", "Defense Forme Deoxys", "Normal Forme Deoxys", "Speed Forme Deoxys", "Turtwig", "Grotle", "Torterra", "Chimchar", "Monferno", "Infernape", "Piplup", "Prinplup", "Empoleon", "Starly", "Staravia", "Staraptor", "Bidoof", "Bibarel", "Kricketot", "Kricketune", "Shinx", "Luxio", "Luxray", "Budew", "Roserade", "Cranidos", "Rampardos", "Shieldon", "Bastiodon", "Plant Burmy", "Sandy Burmy", "Trash Burmy", "Plant Wormadam", "Sandy Wormadam", "Trash Wormadam", "Mothim", "Combee", "Vespiquen", "Pachirisu", "Buizel", "Floatzel", "Cherubi", "Overcast Cherrim", "Sunny Cherrim", "East Sea Shellos", "West Sea Shellos", "East Sea Gastrodon", "West Sea Gastrodon", "Ambipom", "Drifloon", "Drifblim", "Buneary", "Lopunny", "Mismagius", "Honchkrow", "Glameow", "Purugly", "Chingling", "Stunky", "Skuntank", "Bronzor", "Bronzong", "Bonsly", "Mime Jr", "Happiny", "Chatot", "Spiritomb", "Gible", "Gabite", "Garchomp", "Munchlax", "Riolu", "Lucario", "Hippopotas", "Hippowdon", "Skorupi", "Drapion", "Croagunk", "Toxicroak", "Carnivine", "Finneon", "Lumineon", "Mantyke", "Snover", "Abomasnow", "Weavile", "Magnezone", "Lickilicky", "Rhyperior", "Tangrowth", "Electivire", "Magmortar", "Togekiss", "Yanmega", "Leafeon", "Glaceon", "Gliscor", "Mamoswine", "Porygon Z", "Gallade", "Probopass", "Dusknoir", "Froslass", "Fan Rotom", "Frost Rotom", "Heat Rotom", "Mow Rotom", "Rotom", "Wash Rotom", "Uxie", "Mesprit", "Azelf", "Dialga", "Palkia", "Heatran", "Regigigas", "Giratina Altered Forme", "Giratina Origin Forme", "Cresselia", "Phione", "Manaphy", "Darkrai", "Land Shaymin", "Sky Shaymin", "Arceus Bug Forme", "Arceus Dark Forme", "Arceus Dragon Forme", "Arceus Electric Forme", "Arceus Fairy Forme", "Arceus Fighting Forme", "Arceus Fire Forme", "Arceus Flying Forme", "Arceus Ghost Forme", "Arceus Grass Forme", "Arceus Ground Forme", "Arceus Ice Forme", "Arceus", "Arceus Poison Forme", "Arceus Psychic Forme", "Arceus Rock Forme", "Arceus Steel Forme", "Arceus Water Forme", "Meltan", "Melmetal"

with open('simple.json', 'r') as f:
    stats = json.load(f)

data = pd.read_csv('cpm.csv').values.tolist()
cpm = {k:v for (k,v) in data}

def cp(name, a, d, s, level):
    base = stats[name]
    attack = a + base['attack']
    defense = d + base['defense']
    stamina = s + base['stamina']
    c = math.floor((attack * (defense**0.5) * (stamina**0.5) * (cpm[level]**2)) / 10)
    return c if c > 10 else 10

def product(pkm, a, d, s, lvl=0):
    if lvl == 0:
        lvl = max_lvl(pkm, a=a, d=d, s=s)
    multiplier = cpm[lvl]

    attack, defense, stamina = stats[pkm]['attack'], stats[pkm]['defense'], stats[pkm]['stamina']

    attack = (attack + a) * multiplier
    defense = (d + defense) * multiplier
    stamina = int((s + stamina) * multiplier)

    return attack * defense * stamina

def sum_it(pkm, a, d, s, lvl=0):
    if lvl == 0:
        lvl = max_lvl(pkm, a=a, d=d, s=s)
    multiplier = cpm[lvl]

    attack, defense, stamina = stats[pkm]['attack'], stats[pkm]['defense'], stats[pkm]['stamina']

    attack = (attack + a) * multiplier
    defense = (d + defense) * multiplier
    stamina = int((s + stamina) * multiplier)

    return attack + defense + stamina

def max_lvl(pkm, a=0, d=0, s=0):
    for i in range(2, 81):
        if cp(pkm, a, d, s, i/2) > 1500:
            return (i-1)/2
    return 40

def format_pkm(pkm, a, d, s, lvl):
    return f'{pkm}: {lvl}, {a}/{d}/{s}'

class Pkm():
    def __init__(self, name, a, d, s, lvl):
        self.name = name
        self.a = a
        self.d = d
        self.s = s
        self.lvl = lvl
        self.product = product(name, a, d, s, lvl)
        self.maxlvl = max_lvl(name, a=a, d=d, s=s)
        self.maxcp = cp(name, a, d, s, self.maxlvl)
    def __repr__(self):
        return f'{self.name} {self.maxlvl} ({self.maxcp}): L{self.lvl}, {self.a}/{self.d}/{self.s}'
    def ivs(self):
        return (self.a, self.d, self.s)
    def ivs_f(self):
        return f'{self.a}/{self.d}/{self.s}'
    def ivsl_f(self):
        return f'{self.a}/{self.d}/{self.s} {self.lvl}'
    def __lt__(self, other):
        return self.lvl < other.lvl
    def __hash__(self):
        return hash(str(self))
    def export(self):
        return self.name, self.a, self.d, self.s, self.lvl
    def percent(self):
        return f'{100 - 100*abs(best_product(self.name)[1] - self.product)/self.product:.2f}%'

def best_product(pkm):
    best = 0
    st = ""
    lvl = max_lvl(pkm)
    for lvl in range(2, int(lvl*2)+1):
        # print(lvl)
        for a in range(0, 16):
            for d in range(0, 16):
                for s in range(0, 16):
                    if cp(pkm, a, d, s, lvl/2) <= 1500:
                        p = product(pkm, a, d, s, lvl/2)
                        if p > best:
                            st = Pkm(pkm, a, d, s, lvl/2)
                            best = p
    return st, best 

def best_sum(pkm):
    best = 0
    st = ""
    lvl = max_lvl(pkm)
    for lvl in range(2, int(lvl*2)+1):
        # print(lvl)
        for a in range(0, 16):
            for d in range(0, 16):
                for s in range(0, 16):
                    if cp(pkm, a, d, s, lvl/2) <= 1500:
                        p = sum_it(pkm, a, d, s, lvl/2)
                        if p > best:
                            st = Pkm(pkm, a, d, s, lvl/2)
                            best = p
    return st, best 

def worst_product(pkm):
    all_stats = dict()
    for a in range(0, 16):
            for d in range(0, 16):
                for s in range(0, 16):
                    lvl = max_lvl(pkm, a=a, s=s, d=d)
                    all_stats[(a,d,s,lvl)] = product(pkm, a, d, s, lvl)
    min_product = product(pkm, 15, 15, 15, 40)
    min_ivs = (15, 15, 15, 40)
    for k, v in all_stats.items():
        a,d,s,lvl = k
        p = product(pkm, a, d, s, lvl)
        if p < min_product:
            min_product = p
            min_ivs = a,d,s,lvl

    return Pkm(pkm, *min_ivs), min_product

def worst_sum(pkm):
    all_stats = dict()
    for a in range(0, 16):
            for d in range(0, 16):
                for s in range(0, 16):
                    lvl = max_lvl(pkm, a=a, s=s, d=d)
                    all_stats[(a,d,s,lvl)] = sum_it(pkm, a, d, s, lvl)
    min_sum = sum_it(pkm, 15, 15, 15, 40)
    min_ivs = (15, 15, 15, 40)
    for k, v in all_stats.items():
        a,d,s,lvl = k
        p = sum_it(pkm, a, d, s, lvl)
        if p < min_sum:
            min_sum = p
            min_ivs = a,d,s,lvl

    return Pkm(pkm, *min_ivs), min_sum

def better_than(pkm, a, d, s, l=1):
    lvl = max_lvl(pkm, a=a, d=d, s=s)
    if l > lvl:
        return []
    p = product(pkm, a, d, s, lvl)

    l = []
    lvl = max_lvl(pkm)
    for lvl in range(2, int(lvl*2)+1):
        for a in range(0, 16):
            for d in range(0, 16):
                for s in range(0, 16):
                    if cp(pkm, a, d, s, lvl/2) <= 1500:
                        if p < product(pkm, a, d, s, lvl/2):
                            l.append((product(pkm, a, d, s, lvl/2), Pkm(pkm, a, d, s, lvl/2)))
    return [x[1].ivsl_f() for x in sorted(l, reverse=True)]

def rank(pkm, a, d, s):
    return len(better_than(pkm, a, d, s)) + 1

def compare(l):
    dic = dict()
    for x in l:
        name, a, d, s, lvl = x.export()
        lvl = max_lvl(name, a=a, d=d, s=s)
        p = product(name, a, d, s, lvl)
        dic[x] = rank(name, a, d, s)
    l = sorted(list(dic.items()), key=operator.itemgetter(1), reverse=False)
    return l

def comp_txt(name):
    with open("ivs_tmp.txt", 'r') as f:
        ivs = f.read().split('\n')
    ivs = [tuple(int(x) for x in y.split(' ')) for y in ivs]
    lvl = max_lvl(name)
    l = [Pkm(name, *x, lvl) for x in ivs]
    return compare(l)

if __name__ == '__main__':
    name = 'Melmetal'
    lvl = 4


    p1 = Pkm(name, 0, 13, 8, 2)
    p2 = Pkm(name, 3, 14, 12, 2)
    p3 = Pkm(name,0, 14, 9, 2)
    p4 = Pkm(name, 3, 10, 10, 2)
    p5 = Pkm(name, 0, 9, 14, 2)

    l = [p1,p2,p3,p4,p5]
    # print(compare(l))
    # pprint(comp_txt('Infernape'))
    # print(max_lvl('Infernape'))
    # print(cp('Trapinch', 0, 0, 0, 28))

    # cc = comp_txt(name)
    # print(cc)
    # top = cc[0]
    # print(top[0].percent())
    # print(top)

    name = 'Empoleon'
    # print(rank(name, 1, 12, 14))
    print(cp(name, 1, 12, 14, 15))

    # print(worst_product(name))
    # print(best_product(name))
    # print(worst_sum(name))
    # print(best_sum(name))