import networkx as nx
import pandas as pd
from netbone.backbone import Backbone
from netbone.filters import boolean_filter
# algo: minimum_spanning_tree
# calculating MSP

def maximum_spanning_tree(data):
    if isinstance(data, pd.DataFrame):
        G = nx.from_pandas_edgelist(data, edge_attr='weight', create_using=nx.Graph())
    elif isinstance(data, nx.Graph):
        G = data.copy()
    else:
        print("data should be a panads dataframe or nx graph")
        return


    df = nx.to_pandas_edgelist((G))
    df['distance'] = df.apply(lambda row : 1/row['weight'], axis = 1)

    nx.set_edge_attributes(G, nx.get_edge_attributes(nx.from_pandas_edgelist(df, edge_attr='distance'), 'distance'), name='distance')
    msp = nx.minimum_spanning_tree(G, weight='distance')
    nx.set_edge_attributes(G, True, name='msp_backbone')

    missing_edges = {edge: {"msp_backbone": False} for edge in set(G.edges()).difference(set(msp.edges()))}
    nx.set_edge_attributes(G, missing_edges)

    return Backbone(G, name="Maximum Spanning Tree", column="msp_backbone", ascending=False, filters=[boolean_filter])



