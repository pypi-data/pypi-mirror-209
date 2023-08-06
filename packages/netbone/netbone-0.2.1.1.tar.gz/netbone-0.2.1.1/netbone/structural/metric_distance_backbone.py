
import pandas as pd
import networkx as nx
from netbone.structural.distanceclosure import backbone as dc_backbone
from netbone.backbone import Backbone
from netbone.filters import boolean_filter

def metric_distance_backbone(data):
    G = data.copy()
    if isinstance(data, pd.DataFrame):
        G = nx.from_pandas_edgelist(data, edge_attr='weight', create_using=nx.Graph())

    for u, v in G.edges():
        G[u][v]['distance'] = 1/G[u][v]['weight']

    m_backbone = dc_backbone.metric_backbone(G, weight='distance')
    nx.set_edge_attributes(G, True, name='metric_distance_backbone')

    missing_edges = {edge: {"metric_distance_backbone": False} for edge in set(G.edges()).difference(set(m_backbone.edges()))}
    nx.set_edge_attributes(G, missing_edges)

    return Backbone(G, name="Metric Distance Filter", column="metric_distance_backbone", ascending=False, filters=[boolean_filter])

#
# def metric_distance_backbone(data):
#     # distance closure
#
#     if isinstance(data, pd.DataFrame):
#         #create graph from the edge list
#         labeled_G = nx.from_pandas_edgelist(data, edge_attr='weight', create_using=nx.Graph())
#     else:
#         labeled_G=data
#
#     #convert node labels to integers and store the labels as attributes and get the label used for mapping later
#     G = nx.convert_node_labels_to_integers(labeled_G, label_attribute='name')
#     mapping_lables = nx.get_node_attributes(G, name='name')
#
#     #create the adjacency matrix of the graph
#     W = nx.adjacency_matrix(G).todense()
#
#     #calculate the proximity matrix using the weighted jaccard algorithm
#     P = dc_distance.pairwise_proximity(W, metric='jaccard_weighted')
#
#     #convert the proximity matrix to a distance matrix
#     D = np.vectorize(dc_utils.prox2dist)(P)
#
#     #create a distance graph from the distance matrix containing only the edges observed in the original network
#     DG = nx.from_numpy_matrix(D)
#     for u,v in DG.edges():
#         edge = (u,v)
#         if edge not in G.edges():
#             DG.remove_edge(u, v)
#
#     #apply the distance closure algorithm to obtain the metric and ultrametric backbones
#     m_backbone = dc.distance_closure(DG, kind='metric', weight='weight', only_backbone=True)
#
#     #relabel the graphs with the original labels
#     m_backbone = nx.relabel_nodes(m_backbone, mapping_lables)
#
#     return Backbone(m_backbone, name="Metric Distance Filter", column="metric_distance_backbone")