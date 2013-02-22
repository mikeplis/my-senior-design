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
G.add_edges_from(bank_edges, contract_value = 1.0)

edges = G.edges(data=True)
nodes = G.nodes(data=True)

num_edges = len(edges)
constants = numpy.empty(num_edges)
coefficients = numpy.diag(numpy.ones(num_edges))

"""for i, edge in enumerate(edges):
    node = nodes.index(edge[0])
    neighbor = edge[1]
    contract_value = edge[2]['contract_value']
    #sum_contracts = node.sum_contracts
    
    sum_contracts = 5.0"""





