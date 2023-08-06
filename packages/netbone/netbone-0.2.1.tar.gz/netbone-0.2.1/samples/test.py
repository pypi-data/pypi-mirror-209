import math

import networkx as nx
import netbone as nb
import netbone.compare as comp
from netbone.filters import fraction_filter, threshold_filter, boolean_filter
from netbone.visualize import plot_radar, plot_distribution, plot_props
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from netbone.compare import Compare
from netbone.measures import  degrees, edge_fraction, weight_fraction, node_fraction, weights
import pyreadr

g = nx.karate_club_graph()

result = pyreadr.read_r('backbone2_tutorial.RData')
g = nx.from_pandas_adjacency(result['airport'])

# g1 = nb.doubly_stochastic(g)
# nx.draw_networkx(boolean_filter(g1))
# plt.show()
# g = nx.from_pandas_edgelist(pd.read_csv('airports.csv'), edge_attr='weight')

# import networkx as nx
# import pyreadra
#
# result = pyreadr.read_r('backbone2_tutorial.RData')
# g = nx.from_pandas_adjacency(result['airport'])
# # g = nx.karate_club_graph()
# # g1 = nb.global_threshold()
# # g1 = nb.disparity(g)
# # g1 = nb.noise_corrected()
# # g1 = nb.marginal_likelihood()
# # g1 = nb.lans()
# # g1 = nb.ecm()
# #
# # g1 = nb.maximum_spanning_tree()
# # g1 = nb.doubly_stochastic()
# # g1 = nb.high_salience_skeleton()
# # g1 = nb.h_backbone()
# # g1 = nb.metric_distance_backbone()
# # g1 = nb.ultrametric_distance_backbone()
# # g1 = nb.modularity_backbone(g)
# #
# # print(g1.to_dataframe())
#
# # b = threshold_filter(g1, 0.8)
# # b = boolean_filter(g1)
# # b = fraction_filter(g1, 0.8)
#
#
#
compare = Compare()
compare.set_network(g)
compare.set_filter(threshold_filter, [0.05]*5)

g1 = nb.noise_corrected(g)
g2 = nb.disparity(g)
g3 = nb.marginal_likelihood(g)
g4 = nb.lans(g)
g5 = nb.ecm(g)
g6 = nb.global_threshold(g)


# compare.add_backbone(g1)
# compare.add_backbone(g2)
# compare.add_backbone(g3)
# compare.add_backbone(g4)
# compare.add_backbone(g5)
# # #
# compare.add_property("Edge Fraction", edge_fraction)
# compare.add_property("Node Fraction", node_fraction)
# compare.add_property("Weight Fraction", weight_fraction)
# #
# properties = compare.properties()
# # # print(properties)
# # #
# plot_radar(properties, title='Karate Club Network')


compare = Compare()

compare.set_network(g)

# define the array of fractions
fractions = [0.1, 0.2, 0.3, 0.4, 0.5]#, 0.6, 0.7, 0.8, 0.9, 1]
compare.set_filter(fraction_filter, [0.1]*6)

compare.add_backbone(g1)
compare.add_backbone(g2)
compare.add_backbone(g3)
compare.add_backbone(g4)
compare.add_backbone(g5)
compare.add_backbone(g6)

compare.add_property('Node Fraction', node_fraction)
compare.add_property('Edge Fraction', edge_fraction)
compare.add_property('Weight Fraction', weight_fraction)

def average_degree(original, graph):
    values = degrees(graph)
    return sum(values)/len(values)

def density(original, graph):
    return round(nx.density(graph), 4)

compare.add_property('Average Degree', average_degree)
compare.add_property('Density', density)

# compute the properties progression and preview them:
props_results = compare.properties_progression(fractions)

plot_props(props_results, 'Airports')

results = compare.cumulative_distribution('Weight', weights)

plot_distribution(results, title='Aiprots')





# #
#
#
# results = compare.cumulative_distribution('Weight', weights)
# plot_distribution(results, title='Karate Club Network')
# # print(results)
#
#
#
#
#
#
# fractions = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
# results = compare.properties_progression(fractions)
# print(results['Node Fraction'])
# plot_props(results, 'Karate Club Network')
#
#
#
#
#
#
#
# #
