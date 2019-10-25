from itertools import permutations
import grequests

s  ='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
s = list(s)
base = 'https://pokemongo.gamepress.gg/sites/pokemongo/files/styles/240w/public/flork-images/'
for i in range(1, 5):
    print(i)
    rs = (grequests.get(f'{base}{"".join([str(y) for y in x])}.png') for x in permutations(s,i))
    requests = grequests.map(rs)
    for response in requests:
        if response:
            print(response.url)



urls = [
    'http://www.heroku.com',
    'http://python-tablib.org',
    'http://httpbin.org',
    'http://python-requests.org',
    'http://kennethreitz.com'
]

rs = (grequests.get(u) for u in urls)
requests = grequests.map(rs)
for response in requests:
    print(response)