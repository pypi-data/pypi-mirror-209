import networkx as nx
import pandas as pd
import numpy as np

def zscore_backbone(data):
    is_graph=False

    if isinstance(data, pd.DataFrame):
        G = nx.from_pandas_edgelist(data, edge_attr='weight', create_using=nx.Graph())
    elif isinstance(data, nx.Graph):
        G = data
        is_graph=True
    else:
        print("data should be a panads dataframe or nx graph")
        return

    for node in G.nodes():
        calculate_z_scores(node, G)

    return G, "ZScore_backbone"



def calculate_z_scores(node, G, border=1):
    #extract the second neighborhood of the given node
    g = nx.Graph()
    for neighbor in G.neighbors(node):
        g.add_edge(node, neighbor,weight=G[node][neighbor]['weight'])
        for nneighbor in G.neighbors(neighbor):
            g.add_edge(nneighbor, neighbor,weight=G[nneighbor][neighbor]['weight'])

    #extract all the weight of the second neighborhood
    neighbourhood_weights = list(nx.get_edge_attributes(g, 'weight').values())

    #duplicate the edges when reaching the border
    if G.degree(node) <= border:
        #print(neighbourhood_weights)
        neighbourhood_weights = neighbourhood_weights*2
        #print(neighbourhood_weights)


    #calculate mean of the weights in the second neighbourhood
    mean = np.mean(neighbourhood_weights)

    #calculate standard deviation of the weights in the second neighbourhood
    stdv = np.std(neighbourhood_weights)

    #loop through the edges of the node and assign the z-scores
    for u,v,weight in g.edges(data='weight'):
        z_score = (weight - mean) / stdv
        if 'z_score'in G[u][v]:
            G[u][v]['z_score'] = max(G[u][v]['z_score'], z_score)
        else:
            G[u][v]['z_score'] = z_score


# g = nx.karate_club_graph()
# b = zscore_backbone(g, border=1)
#
# print(b.edges(data=True))
