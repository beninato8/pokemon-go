from itertools import product
import requests

s  ='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
s = list(s)
base = 'https://pokemongo.gamepress.gg/sites/pokemongo/files/styles/240w/public/flork-images/'
for i in range(1, 5):
    for x in product(s,repeat=i):
        name = ''.join([str(y) for y in x])
        url = f'{base}{name}.png'
        if requests.get(url).status_code == 200:
            print(name)

