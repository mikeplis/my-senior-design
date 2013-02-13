import networkx as nx
from networkx.readwrite import json_graph
import itertools
import numpy
import matplotlib.pyplot as plt
import json

G = nx.DiGraph()
banks = ['Bank 1', 'Bank 2', 'Bank 3', 'Bank 4', 'Bank 5']
G.add_nodes_from(banks, capital = 0, shock = 0)
bank_edges = itertools.permutations(banks, 2)
G.add_edges_from(bank_edges, payment = 1.0)

data = json_graph.node_link_data(G)
s = json.dumps(data)

