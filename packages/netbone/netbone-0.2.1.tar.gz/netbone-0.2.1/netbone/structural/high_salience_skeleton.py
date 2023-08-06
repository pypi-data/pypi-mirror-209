
from collections import defaultdict
import networkx as nx
import pandas as pd
import warnings
from netbone.backbone import Backbone
from netbone.filters import boolean_filter, threshold_filter, fraction_filter

# change distance
def high_salience_skeleton(data):
    if isinstance(data, pd.DataFrame):
        graph = nx.from_pandas_edgelist(data, edge_attr='weight', create_using=nx.Graph())
    elif isinstance(data, nx.Graph):
        graph = data.copy()
    else:
        print("data should be a panads dataframe or nx graph")
        return

    wes= nx.get_edge_attributes(graph, 'weight')
    values = {pair:1/wes[pair] for pair in wes}
    nx.set_edge_attributes(graph, values, name='distance')

    nx.set_edge_attributes(graph, 0, name='score')

    for source in graph.nodes():
        tree = nx.single_source_dijkstra(graph, source, cutoff=None, weight='distance')[1]
        node_tree_scores = dict()

        paths = list(tree.values())[1:]
        for path in paths:
            for i in range(len(path) - 1):
                node_tree_scores[(path[i], path[i+1])] = 1

        for u,v in node_tree_scores:
            graph[u][v]['score'] +=1

    scores= nx.get_edge_attributes(graph, 'score')
    N = len(graph)
    score_values = dict()
    backbone_edges = dict()
    for pair in scores:
        score_values[pair] = scores[pair]/N
        if scores[pair]/N > 0.8:
            backbone_edges[pair] = True
        else:
            backbone_edges[pair] = False

            # score_values = {pair:scores[pair]/N for pair in scores}
    nx.set_edge_attributes(graph, score_values, name='score')
    nx.set_edge_attributes(graph, backbone_edges, name='high_salience_skeleton')

    # for u,v in graph.edges():
    #     if graph[u][v]['score']>=0.8:
    #         graph[u][v]['high_salience_skeleton'] = True
    #     else:
    #         graph[u][v]['high_salience_skeleton'] = False
    return Backbone(graph, name="High Salience Skeleton Filter", column="high_salience_skeleton", ascending=False, filters=[boolean_filter, threshold_filter, fraction_filter])
