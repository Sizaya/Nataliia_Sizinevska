import networkx as nx
import matplotlib.pyplot as plt

with open('cities.csv', 'r') as file:
    cities = [file.readline().split(",") for line in file]

g = nx.Graph()
for edge in cities:
    g.add_edge(edge[0], edge[1], weight=int(edge[2]))

pos = nx.spring_layout(g)
nx.draw_networkx(g, pos)
plt.title('Cities')
plt.show()