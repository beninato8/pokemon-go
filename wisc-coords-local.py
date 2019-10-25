from geopy.distance import geodesic
from pprint import pprint
from itertools import permutations
from tqdm import tqdm
import gmplot 
from math import cos, sin, atan2, sqrt
import time
import re

home = (43.077589, -89.414075)

with open('wisc-coords-local.txt', 'r') as f:
    text = f.read()

def dist_between(coords, home=home):
    return geodesic(coords, home).meters

coords = dict()
for i, x in enumerate(text.split('\n')):
    if x == '':
        continue
    tmp = re.split(r'0{4},', x)
    lat = float(tmp[0])
    lon = float(tmp[1])
    dist = dist_between((lat, lon))
    if dist > 4700:
        continue
    name = tmp[2].lower()
    coords[name] = dict()
    coords[name]['coords'] = (lat, lon)
    coords[name]['distance'] = dist
# print(len(coords))
# exit()
# pprint(coords.items())
for k,v in sorted(coords.items(), key = lambda k: k[1]['distance']):
    print(f"{v['coords'][0]},{v['coords'][1]},{k}")
# exit()
print("43.074757,-89.380006,afk 4 stop")
print("43.076735,-89.413106,afk 2 stop 2 gym")
exit()

def center_geolocation(coords):
    lats = []
    lons = []
    for k,v in coords.items():
      lats.append(v['coords'][0])
      lons.append(v['coords'][1])

    return (sum(lats)/len(lats), sum(lons)/len(lons))

def fac(n):
    if n < 2:
        return 1
    return n * fac(n-1)

lats = [v['coords'][0] for v in coords.values()]
lons = [v['coords'][1] for v in coords.values()]

center = center_geolocation(coords)
gmap3 = gmplot.GoogleMapPlotter(center[0], center[1], 13) 

gmap3.scatter(lats, lons, '# FF0000', 
                              size = 40, marker = False )
# gmap3.plot(lats, lons,  
#            'cornflowerblue', edge_width = 2.5) 
gmap3.draw("/Users/Nicholas/Github/pokemon-go/map.html")