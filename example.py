import networkx as nx
import itertools
import numpy
import matplotlib.pyplot as plt

G = nx.DiGraph()
banks = ['Bank 1', 'Bank 2', 'Bank 3', 'Bank 4', 'Bank 5']
G.add_nodes_from(banks, capital = 0, shock = 0)
bank_edges = itertools.permutations(banks, 2)
G.add_edges_from(bank_edges, payment = 1.0)

"""pos = nx.spring_layout(G)
nx.draw(G, pos, node_color='#A0CBE2')
plt.show()"""
