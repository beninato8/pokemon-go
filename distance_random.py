from geopy.distance import geodesic
from pprint import pprint
from itertools import permutations
from tqdm import tqdm
import gmplot 
from math import cos, sin, atan2, sqrt
import time
from random import shuffle

with open('coords.txt', 'r') as f:
    text = f.read()
# print(text)
coords = []
for i, x in enumerate(text.split('\n')):
    if x == '':
        continue
    tmp = x.replace(' ', '').split(',')
    lat = float(tmp[0])
    lon = float(tmp[1])
    coords.append((i, lat, lon))
# coords = coords[0:4]
edge_objects = {}
for x in coords:
    edge_objects[x[0]] = dict()
for x in coords:
    for y in coords:
        if x != y:
            edge_objects[x[0]][y[0]] = geodesic((x[1], x[2]), (y[1],y[2])).meters

def distance(points):
    previous = 0
    d = 0
    for x in points:
        d += edge_objects[previous][x]
        previous = x
    return d

def center_geolocation(geolocations):
    lats = []
    lons = []
    for lat, lon in geolocations:
      lats.append(lat)
      lons.append(lon)

    return (sum(lats)/len(lats), sum(lons)/len(lons))

def fac(n):
    if n < 2:
        return 1
    return n * fac(n-1)

t = fac(len(coords) - 1)
print(f'{t} iterations')
seconds_int = int(t/450000)
seconds = time.strftime('%H:%M:%S', time.gmtime(seconds_int))
print(seconds, end='')
if seconds_int > 180:
    print(f' will take too long')
    exit()
print()
shortest_size = 9999999999999999999999999999999
shortest_path = []
points = list(range(1, len(coords)))
p = permutations(points)
print()
i = 0
for x in tqdm(p):
# for x in p:
    i += 1
    if i > 10000000:
        break
    size = distance(x)
    if size < shortest_size:
        shortest_size = size
        shortest_path = x

path = [0] + list(shortest_path)

coords_dict = {name:(lat, lon) for (name, lat, lon) in coords}
points = [coords_dict[x] for x in path]

# print(points)
for x in points:
    print(', '.join(str(y) for y in x))
lats = [x[0] for x in points]
lons = [x[1] for x in points]

center = center_geolocation(points)
gmap3 = gmplot.GoogleMapPlotter(center[0], center[1], 13) 

gmap3.scatter(lats, lons, '# FF0000', 
                              size = 40, marker = False )
gmap3.plot(lats, lons,  
           'cornflowerblue', edge_width = 2.5) 
gmap3.draw("/Users/Nicholas/Github/pokemon-go/map.html")