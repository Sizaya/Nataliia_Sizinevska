import networkx as nx

def marshrut(city1, city2):
    weight = 'weight'
    marsh = nx.shortest_path(g, city1, city2, weight=weight)
    length = nx.shortest_path_length(g, city1, city2, weight=weight)
    return marsh, length

with open('cities.csv', 'r') as file:
    cities = [file.readline().split(",") for line in file]

g = nx.Graph()
for edge in cities:
    g.add_edge(edge[0], edge[1], weight=int(edge[2]))

print(marshrut('Netishyn', 'Ternopil'))







