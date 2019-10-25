from geopy.distance import geodesic
import networkx as nx
from matplotlib import pyplot as plt


plt.gca().invert_yaxis()
plt.gca().invert_xaxis()

with open('coords.txt', 'r') as f:
    text = f.read()

coords = []
for i, x in enumerate(text.split('\n')):
    tmp = x.replace(' ', '').split(',')
    lat = float(tmp[0])
    lon = float(tmp[1])
    coords.append((f'Point {i}', lat, lon))

edge_objects = {}
for x in coords:
    for y in coords:
        if x != y and (x, y) not in edge_objects and (y, x) not in edge_objects:
            edge_objects[(x[0], y[0])] = geodesic((x[1], x[2]), (y[1],y[2])).meters

points = [(k[0], k[1], v) for k,v in edge_objects.items()]
# print(points)

G = nx.Graph()

for from_loc, to_loc, dist in points:
    G.add_edge(from_loc, to_loc, distance=dist)

pos = nx.spring_layout(G,k=0.15,iterations=200)
nx.draw(G, pos, with_labels=True)
edge_labels = nx.get_edge_attributes(G,'distance')
nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labels)
nx.draw_networkx_nodes(G, pos, nodelist=list(f'Point {i}' for x in range(len(coords))), node_color='r')
plt.show()
print(list(nx.edge_dfs(G)))













start, coords = coords[0], coords[1:]

# path = []
# d = 0
# close = start
# for i in range(len(coords)):
#     d2 = geodesic(start, coords[i])
#     if i == 0 or d2 < d:
#         d = d2
#         close = coords[i]

# print(close)